### **Scenario 6: Build an ETL Pipeline with Azure Data Factory**

This scenario teaches users how to create an **ETL (Extract, Transform, Load)** pipeline using **Azure Data Factory (ADF)**. The pipeline will extract data from a source (e.g., Azure Blob Storage), transform it using Data Flows, and load it into a destination (e.g., Azure SQL Database).

---

### **1. Objective**
Users will:
1. Create an **Azure Data Factory**.
2. Extract data from Azure Blob Storage.
3. Transform the data using **Mapping Data Flows**.
4. Load the transformed data into an Azure SQL Database.

---

### **2. Prerequisites**
1. **Azure for Students account** with $100 free credits.
2. **Azure SQL Database** created:
   - Set up a free-tier database and note down its **server name**, **username**, and **password**.
3. **Sample Dataset**:
   - A sample CSV or JSON file uploaded to Azure Blob Storage.

---

### **3. Steps**

#### **Step 1: Create an Azure Data Factory**

1. **Log in to Azure Portal**:
   - Go to [Azure Portal](https://portal.azure.com) and sign in.

2. **Navigate to Data Factory**:
   - Search for **Data Factories** in the search bar and click **+ Create**.

3. **Fill in Basic Details**:
   - **Subscription**: Select your subscription.
   - **Resource Group**: Create or select a resource group (e.g., `etl-pipeline-project`).
   - **Region**: Select a region close to your location.
   - **Name**: Enter a unique name (e.g., `user-datafactory`).

4. **Review and Create**:
   - Click **Review + Create**, then **Create** to deploy the Data Factory.

5. **Open Data Factory Studio**:
   - Once deployed, click **Open Azure Data Factory Studio** to launch the Data Factory interface.

---

#### **Step 2: Connect to Data Sources**

##### **A. Create a Linked Service for Blob Storage**
1. In Data Factory Studio, go to the **Manage** tab.
2. Under **Linked Services**, click **+ New**.
3. Select **Azure Blob Storage** and configure:
   - **Name**: Enter a name (e.g., `BlobLinkedService`).
   - **Authentication Method**: Choose **Account Key**.
   - **Storage Account**: Select your Blob Storage account.
4. Test the connection and save.

##### **B. Create a Linked Service for Azure SQL Database**
1. Click **+ New** under **Linked Services**.
2. Select **Azure SQL Database** and configure:
   - **Name**: Enter a name (e.g., `SQLLinkedService`).
   - **Server Name**: Enter your Azure SQL Database server name.
   - **Database Name**: Enter the database name.
   - **Authentication**: Enter the database username and password.
3. Test the connection and save.

---

#### **Step 3: Create an ETL Pipeline**

##### **A. Create a Dataset for Source Data**
1. Go to the **Author** tab and click **+** > **Dataset**.
2. Select **Azure Blob Storage** as the source type.
3. Choose the file format (e.g., CSV).
4. Configure the dataset:
   - **Linked Service**: Select the Blob Storage linked service.
   - **File Path**: Browse and select the file in Blob Storage.

##### **B. Create a Dataset for Destination Data**
1. Create another dataset.
2. Select **Azure SQL Database** as the type.
3. Configure the dataset:
   - **Linked Service**: Select the SQL Database linked service.
   - **Table Name**: Select or create a target table in your SQL database.

##### **C. Add a Data Flow**
1. Go to the **Author** tab and click **+** > **Data Flow**.
2. In the Data Flow canvas:
   - **Source**: Drag and drop a **Source** activity and link it to the Blob Storage dataset.
   - **Transformation**: Add transformations such as:
     - **Filter**: Filter rows based on a condition (e.g., sales > 1000).
     - **Derived Column**: Add or modify columns (e.g., calculate tax as sales * 0.1).
   - **Sink**: Drag and drop a **Sink** activity and link it to the SQL Database dataset.

##### **D. Add the Data Flow to a Pipeline**
1. Create a new **Pipeline** in the Author tab.
2. Add the **Data Flow** activity to the pipeline.
3. Configure the **Data Flow** activity to run the created data flow.

---

#### **Step 4: Test and Run the Pipeline**

1. **Debug the Pipeline**:
   - Click **Debug** in the pipeline to test the ETL process without publishing it.

2. **Publish and Run**:
   - Click **Publish All** to save the pipeline.
   - Trigger the pipeline manually by clicking **Add Trigger** > **Trigger Now**.

3. **Monitor the Pipeline**:
   - Go to the **Monitor** tab to view the pipeline's execution status, duration, and any errors.

---

### **4. Optional Enhancements**

#### **Automate the Pipeline**
- Schedule the pipeline to run daily or hourly using **Triggers**.

#### **Add Data Validation**
- Include validation steps to ensure data integrity before loading it into the destination.

#### **Use Different Destinations**
- Load the transformed data into **Azure Data Lake Storage**, **Power BI**, or **Cosmos DB** instead of SQL.

#### **Real-Time ETL**
- Use **Event-Driven Triggers** to start the pipeline when new files are uploaded to Blob Storage.

---

### **5. Troubleshooting**

| **Issue**                                | **Solution**                                                      |
|------------------------------------------|--------------------------------------------------------------------|
| Pipeline fails to connect to Blob Storage | Verify the linked service connection and ensure the correct file path. |
| SQL Database load fails                  | Ensure the target table exists and matches the transformed data schema. |
| Data transformation errors               | Check the Data Flow transformation logic for invalid operations.   |

---

### **6. Deliverable**
Users should:
1. Share the **SQL query** showing the transformed data in the Azure SQL Database.
2. Provide a screenshot of the **Monitor tab** showing successful pipeline execution.

---

### **7. Learning Outcomes**
Users will:
- Understand how to create and manage an **ETL pipeline**.
- Learn to integrate **Azure Data Factory** with Blob Storage and SQL Database.
- Gain experience with data transformation using **Mapping Data Flows**.
- Explore pipeline automation and monitoring.

---

This hands-on project provides practical experience in building ETL pipelines, a critical skill for modern data engineering. Let me know if you'd like additional details or refinements!