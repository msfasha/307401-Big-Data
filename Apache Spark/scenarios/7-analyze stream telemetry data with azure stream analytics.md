### **Scenario 7: Analyze Telemetry Data with Azure Stream Analytics**

This scenario introduces users to **Azure Stream Analytics**, where they will process streaming data in real-time. Users will simulate telemetry data (e.g., IoT device readings), analyze it using **Stream Analytics**, and output the results to an Azure SQL Database or Blob Storage.

---

### **1. Objective**
Users will:
1. Simulate streaming data using an **Event Hub** or **IoT Hub**.
2. Set up a **Stream Analytics job** to process the data in real-time.
3. Output the analyzed data to **Azure SQL Database** or **Blob Storage**.

---

### **2. Prerequisites**
1. **Azure for Students account** with $100 free credits.
2. An **Azure SQL Database** or **Blob Storage** account for output.
3. **Azure Event Hub** or **IoT Hub** to simulate telemetry data.

---

### **3. Steps**

#### **Step 1: Set Up the Data Input (Simulated Telemetry Data)**

##### **A. Create an Event Hub**
1. **Log in to Azure Portal**:
   - Go to [Azure Portal](https://portal.azure.com) and sign in.

2. **Create a Namespace**:
   - Search for **Event Hubs** in the search bar.
   - Click **+ Create** and fill in the details:
     - **Namespace Name**: Enter a unique name (e.g., `user-eventhub-ns`).
     - **Pricing Tier**: Select **Basic**.
     - **Region**: Choose a region close to you.
   - Click **Review + Create**, then **Create**.

3. **Create an Event Hub**:
   - Navigate to the namespace you created.
   - Under **Entities**, click **Event Hubs** > **+ Event Hub**.
   - Name your Event Hub (e.g., `telemetry-stream`).
   - Leave the default settings and click **Create**.

4. **Access Keys**:
   - Go to **Shared Access Policies** and copy the **Connection String–Primary Key**. You'll use this to send data.

##### **B. Simulate Telemetry Data**
1. Install the **Azure Event Hub Python SDK**:
   - Run:
     ```bash
     pip install azure-eventhub
     ```

2. Create a Python script to send telemetry data:
   ```python
   from azure.eventhub import EventHubProducerClient, EventData
   import time
   import random

   connection_str = "<your_event_hub_connection_string>"
   event_hub_name = "telemetry-stream"

   producer = EventHubProducerClient.from_connection_string(
       conn_str=connection_str, eventhub_name=event_hub_name
   )

   while True:
       with producer:
           data = {
               "device_id": f"device-{random.randint(1, 5)}",
               "temperature": round(random.uniform(20.0, 30.0), 2),
               "humidity": round(random.uniform(40.0, 60.0), 2),
               "timestamp": time.time()
           }
           event_data = EventData(str(data))
           producer.send_batch([event_data])
           print(f"Sent: {data}")
       time.sleep(1)
   ```

3. Run the script to simulate telemetry data being sent to the Event Hub.

---

#### **Step 2: Create a Stream Analytics Job**

1. **Create the Job**:
   - In the Azure Portal, search for **Stream Analytics jobs** and click **+ Create**.
   - Fill in the details:
     - **Name**: Enter a name (e.g., `telemetry-analytics`).
     - **Resource Group**: Select or create a new resource group.
     - **Region**: Choose a region close to you.
     - **Hosting Environment**: Select **Cloud**.
   - Click **Review + Create**, then **Create**.

2. **Add Input**:
   - Navigate to the Stream Analytics job.
   - Under **Inputs**, click **+ Add stream input** > **Event Hub**.
   - Fill in the details:
     - **Input Alias**: `telemetry-input`.
     - **Event Hub Namespace**: Select the namespace you created.
     - **Event Hub Name**: Select your Event Hub.
     - **Authentication Mode**: Select **Connection String** and paste your Event Hub connection string.

3. **Add Output**:
   - Under **Outputs**, click **+ Add** and select:
     - **Azure SQL Database** or **Blob Storage**.
   - Configure the output:
     - For SQL: Enter the database details (server name, database name, credentials).
     - For Blob: Enter the storage account and container details.

4. **Define the Query**:
   - Under **Query**, write a query to process the telemetry data:
     ```sql
     SELECT
         device_id,
         AVG(temperature) AS avg_temperature,
         AVG(humidity) AS avg_humidity,
         System.Timestamp AS event_time
     INTO
         [your-output-alias]
     FROM
         [telemetry-input]
     GROUP BY
         TUMBLINGWINDOW(Duration(second, 10)), device_id
     ```

---

#### **Step 3: Start the Stream Analytics Job**
1. Click **Start** in the job overview.
2. Select **Now** as the start time and confirm.

---

#### **Step 4: Verify the Output**

##### **For Azure SQL Database**:
1. Open the SQL Database in the Azure Portal.
2. Query the results using tools like Azure Data Studio or SSMS:
   ```sql
   SELECT * FROM telemetry_data;
   ```

##### **For Blob Storage**:
1. Navigate to the Blob Storage container.
2. Verify the generated files (e.g., JSON or CSV) containing processed telemetry data.

---

### **4. Optional Enhancements**

#### **Real-Time Dashboard**:
- Connect the Stream Analytics output to **Power BI** for a live dashboard of telemetry data.

#### **Event Hub Partitioning**:
- Enable partitions for high-throughput scenarios and process partitioned data in Stream Analytics.

#### **Alerts**:
- Set alerts for anomalies (e.g., temperature exceeding thresholds) using **Azure Monitor**.

#### **Output to Multiple Destinations**:
- Add multiple outputs (e.g., SQL Database and Power BI) for diverse analytics use cases.

---

### **5. Troubleshooting**

| **Issue**                                | **Solution**                                                      |
|------------------------------------------|--------------------------------------------------------------------|
| No data processed by Stream Analytics    | Check the Event Hub connection string and ensure the data producer is running. |
| Output errors                            | Verify the destination (SQL or Blob) configuration.               |
| Query syntax issues                      | Test the query in the Stream Analytics job editor.                |
| Job fails to start                       | Ensure the Event Hub and Stream Analytics job are in the same region. |

---

### **6. Deliverable**
Users should:
1. Provide a screenshot of the processed data in SQL or Blob Storage.
2. Share the Stream Analytics query used for analysis.

---

### **7. Learning Outcomes**
Users will:
- Understand how to process **real-time streaming data**.
- Learn to integrate **Event Hub**, **Stream Analytics**, and **Azure SQL Database**.
- Gain insights into real-time data pipelines and monitoring.

---

This scenario provides users with a solid introduction to **real-time data processing** in Azure. Let me know if you'd like to expand on this or include more advanced features!