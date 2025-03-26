### **Scenario 14: Automate Data Processing with Azure Data Factory**

This scenario introduces users to creating an automated **data pipeline** using **Azure Data Factory (ADF)**. They will extract data from Azure Blob Storage, transform it using **Mapping Data Flows**, and load the processed data into Azure SQL Database.

---

### **1. Objective**
Users will:
1. Create an **Azure Data Factory**.
2. Build a pipeline to automate data extraction, transformation, and loading (ETL).
3. Schedule and monitor the pipeline for continuous data processing.

---

### **2. Prerequisites**
1. **Azure for Students account** with $100 free credits.
2. **Azure SQL Database**:
   - Set up a free-tier Azure SQL Database.
   - Note the server name, username, and password.
3. **Azure Blob Storage**:
   - A container with a sample dataset (e.g., CSV or Parquet file).

---

### **3. Steps**

#### **Step 1: Create an Azure Data Factory**

1. **Log in to Azure Portal**:
   - Go to [Azure Portal](https://portal.azure.com) and sign in.

2. **Navigate to Data Factory**:
   - Search for **Data Factories** and click **+ Create**.

3. **Fill in Basic Details**:
   - **Resource Group**: Create or select an existing group (e.g., `data-pipeline-project`).
   - **Region**: Select a region close to your location.
   - **Name**: Enter a unique name (e.g., `user-datafactory`).

4. **Review and Create**:
   - Click **Review + Create**, then **Create**.

5. **Open Data Factory Studio**:
   - Navigate to the deployed Data Factory and click **Launch Studio**.

---

#### **Step 2: Connect to Data Sources**

##### **A. Create a Linked Service for Blob Storage**
1. In Data Factory Studio, go to the **Manage** tab.
2. Under **Linked Services**, click **+ New**.
3. Select **Azure Blob Storage** and configure:
   - **Name**: `BlobLinkedService`.
   - **Authentication Method**: Use **Account Key**.
   - **Storage Account**: Select your Blob Storage account.
4. Test the connection and save.

##### **B. Create a Linked Service for Azure SQL Database**
1. Under **Linked Services**, click **+ New**.
2. Select **Azure SQL Database** and configure:
   - **Name**: `SQLLinkedService`.
   - **Server Name**: Enter your Azure SQL Database server name.
   - **Database Name**: Enter the database name.
   - **Authentication**: Provide the username and password.
3. Test the connection and save.

---

#### **Step 3: Build a Data Pipeline**

1. **Navigate to Author**:
   - Go to the **Author** tab and click **+ Pipeline** > **New Pipeline**.

2. **Add a Data Flow Activity**:
   - Drag a **Data Flow** activity into the pipeline canvas.
   - Click **+ New** to create a new data flow.

3. **Configure the Data Flow**:
   - **Source**:
     - Add a source and select the Blob Storage dataset containing the input file.
     - Configure the file path and format (e.g., CSV).
   - **Transformation**:
     - Add a transformation (e.g., **Filter** rows where sales > 1000 or **Derived Column** to calculate new fields like tax).
   - **Sink**:
     - Add a sink and select the Azure SQL Database dataset.
     - Map source columns to destination table columns.

4. **Save and Debug**:
   - Save the data flow and debug it to ensure it works as expected.

---

#### **Step 4: Schedule the Pipeline**

1. **Add a Trigger**:
   - In the pipeline editor, click **Add Trigger** > **New/Edit**.
   - Configure a schedule trigger to run the pipeline at regular intervals (e.g., daily at midnight).

2. **Test the Pipeline**:
   - Manually trigger the pipeline to ensure it processes the data and loads it into the SQL Database.

3. **Monitor the Pipeline**:
   - Go to the **Monitor** tab to track pipeline runs and identify any errors.

---

### **4. Optional Enhancements**

#### **Enable Error Handling**
- Add a **Failure Path** in the pipeline to log errors in a separate Blob Storage container or database table.

#### **Use Parameterized Pipelines**
- Parameterize file paths and table names to make the pipeline reusable for multiple datasets.

#### **Real-Time Data Processing**
- Integrate with **Event Grid** or **Azure Stream Analytics** to process real-time data.

#### **Add Data Validation**
- Use Data Flow expressions to validate data before loading it into the destination.

---

### **5. Troubleshooting**

| **Issue**                                 | **Solution**                                                      |
|-------------------------------------------|--------------------------------------------------------------------|
| Pipeline fails to connect to Blob Storage | Verify the linked service connection and ensure correct access permissions. |
| SQL Database load fails                   | Check the table schema and ensure the source data matches the structure. |
| Pipeline runs slowly                      | Optimize transformations and ensure the compute target has sufficient resources. |
| Schedule trigger doesn’t run              | Verify the time zone settings and active status of the trigger.    |

---

### **6. Deliverable**
Users should:
1. Share screenshots of the pipeline design and successful run status in the Monitor tab.
2. Provide the SQL query output showing the transformed data in Azure SQL Database.

---

### **7. Learning Outcomes**
Users will:
- Understand how to build automated **ETL pipelines** using Azure Data Factory.
- Learn to connect and process data from **Blob Storage** to **SQL Database**.
- Gain experience in transforming and scheduling data workflows.

---

This project equips users with essential skills in building automated data pipelines, a critical aspect of data engineering and cloud-based analytics workflows. Let me know if you'd like further customizations or advanced features!