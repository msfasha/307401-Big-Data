## Creating and Spark EMR Cluster

This document states the steps required to create an EMR Spark cluster on AWS Data Engineering Academy Environment.
- First, we need to start the SandBox environment,
- We need to install EMR cluster with Spark and Jupyter support
- We need to goto the cluster main page and allow all traffic in Properties, EC2 security groups (firewall)
- We can also check the applications tab where we find URLs for different applications

We have the following alternatives to run spark jobs:
- Using putty and the private .ppk file, see below
- Using Livy, see below
- Using JupyerHub using the following credentials:
The username is "jovyan" and the password is "jupyter"
We do not need to add any permissions using the bootstrap actions as stated in a note below


We need to checkout the JupterHub permission requirement presented later.

- Download putty
- Download the ppk, private key file from AWS lab

Use `pscp` with the `.ppk` Private Key

Assuming you used a `.ppk` file to connect via PuTTY, you need to provide that key to `pscp` using the `-i` option.


### 🔧 Use the following `pscp` Command to upload the sample file
Upload the test.py file into the primary node (use the primary node address, you can get that from the EMR cluster main page on AWS, you can find it
in connect using SSH or SMI

```bash
pscp -i C:\Users\me\Downloads\your-key.ppk C:\Users\me\Downloads\test_spark.py hadoop@ec2-54-165-230-165.compute-1.amazonaws.com:/home/hadoop/
```

### 🔁 Be sure to:

* Replace `your-key.ppk` with the actual file name of your private key.

### ✅ After Upload

Once uploaded, SSH into the server using PuTTY, then run:

```bash
spark-submit /home/hadoop/test_spark.py
```




You can also connect using Livy and the REST api
You can also connect to JupyterHub, but apparently we have to include some bootstrap job during clustering installation
In the **AWS Academy sandbox**, when you launch an EMR cluster with **JupyterHub**, it does **not automatically create a default username and password** for you.

### 🔐 Here's what you need to know:

* **You are expected to configure a user/password** when setting up JupyterHub (via bootstrap action or manually).
* Since this step is skipped in the quick wizard setup, the JupyterHub UI becomes **inaccessible unless a user was preconfigured**.

---

### ✅ Recommended Solutions:

#### Option 1: Use **EMR Notebooks** instead

* Instead of using JupyterHub, go to **EMR → Notebooks** in the AWS Console.
* Create an EMR Notebook linked to your running cluster.
* You won’t need login credentials this way.

#### Option 2: Recreate the cluster with a **bootstrap script** to add a user

Use a bootstrap action like this to set a password (just for lab use):

```bash
#!/bin/bash
sudo bash -c 'echo "jupyter:jupyter123" | chpasswd'
```

And make sure you enable **PAM authentication** in JupyterHub config (`/etc/jupyterhub/jupyterhub_config.py`):

```python
c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'
```

---

If you want, I can help you write the exact bootstrap script and show how to attach it when creating the cluster.





---

## Livy Method
Great! Here's a basic example of how to submit a job to **Apache Livy** using its **REST API**, specifically a simple Spark job written in Python.

### 🛠️ Prerequisites

* Apache Livy is up and running (commonly on port `8998`)
* Apache Spark is correctly configured behind Livy
* You can use tools like `curl`, Postman, or Python (`requests` module) to interact with the API

## 🔁 Step-by-Step: Submit a Spark Job via Livy REST API

### ✅ 1. **Start a New Session**

You need a session before submitting code. Example (using Python):

```python
import requests
import json

livy_url = 'http://localhost:8998/sessions'
headers = {'Content-Type': 'application/json'}
data = {'kind': 'pyspark'}

response = requests.post(livy_url, data=json.dumps(data), headers=headers)
session_info = response.json()
session_id = session_info['id']
print(f"Session ID: {session_id}")
```

---

### ✅ 2. **Check Session Status (Optional but Useful)**

```python
status_response = requests.get(f"{livy_url}/{session_id}")
print(status_response.json())
```

Wait until the session status becomes `"idle"` before sending code.

---

### ✅ 3. **Submit Code to Spark**

Example: Submit a simple Python Spark job (e.g., counting elements):

```python
code = {
    'code': 'sc.parallelize([1, 2, 3, 4]).sum()'
}

statements_url = f"{livy_url}/{session_id}/statements"
response = requests.post(statements_url, data=json.dumps(code), headers=headers)
statement_info = response.json()
statement_id = statement_info['id']
print(f"Statement ID: {statement_id}")
```

---

### ✅ 4. **Get the Job Result**

```python
import time

result_url = f"{statements_url}/{statement_id}"

# Polling for result
while True:
    result_response = requests.get(result_url).json()
    if result_response['state'] == 'available':
        break
    time.sleep(1)

print("Result:", result_response['output'])
```

Expected Output:

```json
{
  "status": "ok",
  "execution_count": 0,
  "data": {
    "text/plain": "10.0"
  }
}
```

---

### ✅ 5. **Close the Session**

```python
requests.delete(f"{livy_url}/{session_id}")
```

---

## 🧾 Summary

* You start a session (`POST /sessions`)
* Wait until it's ready
* Submit Spark code (`POST /sessions/{id}/statements`)
* Retrieve results (`GET /sessions/{id}/statements/{statementId}`)
* Clean up by closing the session

Would you like a ready-to-run Python script that does all of this end-to-end?
