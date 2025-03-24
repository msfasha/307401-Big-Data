### **Scenario 9: Train a Machine Learning Model with Azure Machine Learning**

This scenario introduces users to **Azure Machine Learning** (Azure ML), where they will create a workspace, train a simple machine learning model, and deploy it as a web service. This hands-on project demonstrates the end-to-end process of building and deploying a machine learning model in the cloud.

---

### **1. Objective**
Users will:
1. Set up an **Azure Machine Learning Workspace**.
2. Train a simple **classification model** using the Azure ML Studio.
3. Deploy the model as a web service for inference.

---

### **2. Prerequisites**
1. **Azure for Students account** with $100 free credits.
2. Basic knowledge of Python and machine learning.
3. A sample dataset:
   - Use the built-in **Iris dataset** in Azure ML or upload your own dataset.

---

### **3. Steps**

#### **Step 1: Set Up the Azure ML Workspace**

1. **Log in to Azure Portal**:
   - Go to [Azure Portal](https://portal.azure.com) and sign in.

2. **Create a Machine Learning Workspace**:
   - Search for **Machine Learning** in the search bar and click **+ Create**.
   - Fill in the details:
     - **Resource Group**: Create or select an existing group (e.g., `ml-workspace-group`).
     - **Workspace Name**: Enter a name (e.g., `user-ml-workspace`).
     - **Region**: Select a region close to you.
   - Click **Review + Create**, then **Create**.

3. **Launch Azure ML Studio**:
   - Navigate to the created workspace and click **Launch Studio** to open the Azure ML Studio interface.

---

#### **Step 2: Create a Compute Instance**

1. In Azure ML Studio, navigate to **Compute** > **Compute Instances**.
2. Click **+ New** to create a new compute instance.
   - Select an appropriate VM size (e.g., `Standard_DS11_v2` for free tier eligibility).
3. Start the instance once it's created.

---

#### **Step 3: Train a Machine Learning Model**

##### **Option A: Use Automated ML**
1. **Navigate to Automated ML**:
   - Go to **Automated ML** in the Azure ML Studio interface.
2. **Create a New Experiment**:
   - Select or upload a dataset (e.g., Iris dataset).
   - Choose the **target column** (e.g., `Species` for classification).
3. **Configure Settings**:
   - Select **Compute Cluster** as the compute target.
   - Choose the task type (e.g., Classification).
   - Start the experiment.
4. **Review the Results**:
   - After training, review the best-performing model and metrics (e.g., accuracy, F1 score).

##### **Option B: Use a Jupyter Notebook**
1. **Open a Jupyter Notebook**:
   - In Azure ML Studio, open a notebook in your compute instance.
2. **Write the Model Training Code**:
   - Use the following example for training a simple model:
     ```python
     from sklearn.datasets import load_iris
     from sklearn.model_selection import train_test_split
     from sklearn.ensemble import RandomForestClassifier
     from sklearn.metrics import accuracy_score
     import joblib

     # Load data
     iris = load_iris()
     X, y = iris.data, iris.target
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

     # Train model
     model = RandomForestClassifier()
     model.fit(X_train, y_train)

     # Evaluate model
     y_pred = model.predict(X_test)
     print("Accuracy:", accuracy_score(y_test, y_pred))

     # Save the model
     joblib.dump(model, "iris_model.pkl")
     ```
3. **Upload the Model**:
   - Save the trained model as `iris_model.pkl` and register it in the **Models** section of Azure ML Studio.

---

#### **Step 4: Deploy the Model**

1. **Register the Model**:
   - Navigate to **Models** in Azure ML Studio.
   - Click **Register Model** and upload the saved model file.

2. **Create an Inference Endpoint**:
   - Go to **Endpoints** > **Deployments** and click **+ Create**.
   - Choose **Real-Time Endpoint**.
   - Configure the deployment:
     - Select the registered model.
     - Define the compute target (e.g., a compute instance or cluster).
     - Provide an entry script for inference.

   Example **entry script**:
   ```python
   import joblib
   import json
   from azureml.core.model import Model

   def init():
       global model
       model_path = Model.get_model_path("iris_model")
       model = joblib.load(model_path)

   def run(raw_data):
       data = json.loads(raw_data)
       predictions = model.predict(data["input_data"])
       return {"predictions": predictions.tolist()}
   ```

3. **Deploy the Endpoint**:
   - Start the deployment process and wait for the endpoint to be active.

---

#### **Step 5: Test the Deployed Model**

1. **Get the Endpoint URL**:
   - Copy the endpoint URL from the **Endpoints** tab in Azure ML Studio.

2. **Send a Test Request**:
   - Use a tool like Postman or Python to test the endpoint:
     ```python
     import requests
     import json

     url = "<endpoint-url>"
     headers = {"Content-Type": "application/json"}
     data = {"input_data": [[5.1, 3.5, 1.4, 0.2]]}
     response = requests.post(url, headers=headers, json=data)
     print(response.json())
     ```
3. Verify that the response contains predictions (e.g., species classification).

---

### **4. Optional Enhancements**

#### **Use a Custom Dataset**:
- Replace the Iris dataset with a more complex dataset (e.g., customer churn, sales predictions).

#### **Enable Logging and Monitoring**:
- Enable Application Insights for monitoring the model's performance and usage.

#### **Deploy to Azure Kubernetes Service (AKS)**:
- Deploy the model to an AKS cluster for scalable production workloads.

#### **Integrate with Power BI**:
- Use the deployed model for real-time predictions in a Power BI dashboard.

---

### **5. Troubleshooting**

| **Issue**                                | **Solution**                                                      |
|------------------------------------------|--------------------------------------------------------------------|
| Compute instance not starting            | Ensure the VM size is within your subscription limits.             |
| Model deployment fails                   | Check the entry script and dependencies in the environment setup. |
| Endpoint not responding                  | Verify the endpoint URL and check for firewall or authentication issues. |
| Low model accuracy                       | Optimize hyperparameters or use a different algorithm.             |

---

### **6. Deliverable**
Users should:
1. Provide the **endpoint URL** and sample predictions from the deployed model.
2. Share the **training accuracy** and performance metrics.

---

### **7. Learning Outcomes**
Users will:
- Understand how to set up and use **Azure Machine Learning**.
- Train a machine learning model using automated tools or custom scripts.
- Deploy a model as a web service and test it with real-time data.
- Gain experience with cloud-based machine learning workflows.

---

This hands-on project provides practical experience in building and deploying machine learning models with **Azure Machine Learning**, preparing users for real-world applications. Let me know if you'd like additional details or advanced features!