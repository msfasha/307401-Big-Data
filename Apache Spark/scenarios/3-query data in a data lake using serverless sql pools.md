### **Scenario 3: Query Data in a Data Lake Using Serverless SQL Pools**

This scenario introduces users to **Azure Synapse Analytics Serverless SQL Pools**, enabling them to query raw data directly from a **Data Lake** without needing to import or move the data.

---

### **1. Objective**
Users will:
1. Create a **Data Lake (Azure Storage Account)**.
2. Upload a sample dataset to the Data Lake.
3. Query the dataset using **Synapse Serverless SQL Pools**.
4. Perform basic data analysis.

---

### **2. Prerequisites**
1. **Azure for Students account** with $100 free credits.
2. A sample dataset:
   - Example: Download a public dataset from [Kaggle Datasets](https://www.kaggle.com/datasets) or use a CSV/Parquet file (e.g., sales data, IoT logs).
3. Access to **Azure Portal**: [https://portal.azure.com](https://portal.azure.com).

---

### **3. Steps**

#### **Step 1: Create a Storage Account**
1. **Log in to Azure Portal**:
   - Go to [Azure Portal](https://portal.azure.com) and sign in.

2. **Navigate to Storage Accounts**:
   - Search for **Storage accounts** in the search bar.
   - Click **+ Create**.

3. **Fill in Basic Details**:
   - **Subscription**: Select your subscription.
   - **Resource Group**: Create or select a resource group (e.g., `datalake-project`).
   - **Storage Account Name**: Enter a globally unique name (e.g., `userdatalake123`).
   - **Region**: Choose a region close to your location.
   - **Performance**: Select **Standard**.
   - **Redundancy**: Choose **Locally Redundant Storage (LRS)**.

4. **Enable Hierarchical Namespace**:
   - In the **Advanced** tab, enable **Data Lake Storage Gen2 (Hierarchical Namespace)**.

5. **Review and Create**:
   - Click **Review + Create**, then **Create** to deploy the storage account.

---

#### **Step 2: Upload a Sample Dataset**
1. **Navigate to the Storage Account**:
   - Go to the newly created storage account.

2. **Create a Container**:
   - Click on **Containers** under **Data Storage**.
   - Create a new container (e.g., `sales-data`) and set **Public Access Level** to **Private**.

3. **Upload the Dataset**:
   - Open the container and click **+ Upload**.
   - Select a dataset file (e.g., `sales.csv` or `sales.parquet`).
   - Click **Upload**.

---

#### **Step 3: Set Up Synapse Analytics Workspace**
1. **Create a Synapse Workspace**:
   - In the Azure Portal, search for **Azure Synapse Analytics** and click **+ Create**.
   - Fill in the details:
     - **Resource Group**: Select the same group as the storage account.
     - **Workspace Name**: Enter a name (e.g., `user-synapse-workspace`).
     - **Data Lake Storage Gen2**: Link the previously created storage account.
   - Click **Review + Create**, then **Create**.

2. **Launch Synapse Studio**:
   - Once the workspace is created, click **Launch Synapse Studio** from the Synapse Analytics overview page.

---

#### **Step 4: Query Data Using Serverless SQL Pools**
1. **Create a Linked Service**:
   - In Synapse Studio, navigate to the **Manage** tab > **Linked Services**.
   - Create a new linked service for the storage account.

2. **Access the Dataset**:
   - Go to the **Data** tab > **Linked**.
   - Navigate to the storage account and locate the uploaded dataset.

3. **Run an Ad-Hoc Query**:
   - Go to the **Develop** tab and create a new SQL script.
   - Use the following query to read the dataset:
     ```sql
     SELECT TOP 10 *
     FROM OPENROWSET(
         BULK 'https://userdatalake123.dfs.core.windows.net/sales-data/sales.csv',
         FORMAT = 'CSV',
         PARSER_VERSION = '2.0'
     ) AS [result];
     ```

4. **Analyze the Results**:
   - Run the query and review the results in the output pane.

---

#### **Step 5: Perform Basic Data Analysis**
1. **Filter and Aggregate Data**:
   - Example: Calculate total sales by region.
     ```sql
     SELECT region, SUM(sales_amount) AS total_sales
     FROM OPENROWSET(
         BULK 'https://userdatalake123.dfs.core.windows.net/sales-data/sales.csv',
         FORMAT = 'CSV',
         PARSER_VERSION = '2.0'
     ) AS [data]
     GROUP BY region;
     ```

2. **Save the Query Results**:
   - Save query results to a new CSV file in the Data Lake for further analysis.

---

### **4. Optional Enhancements**

#### **Use a Parquet File**:
- Convert the CSV dataset to **Parquet** for faster query performance and lower storage costs.

#### **Create Views**:
- Create a reusable view to simplify queries:
  ```sql
  CREATE VIEW sales_summary AS
  SELECT region, SUM(sales_amount) AS total_sales
  FROM OPENROWSET(
      BULK 'https://userdatalake123.dfs.core.windows.net/sales-data/sales.csv',
      FORMAT = 'CSV',
      PARSER_VERSION = '2.0'
  ) AS [data]
  GROUP BY region;
  ```

#### **Integrate with Power BI**:
- Use Power BI to visualize the query results directly from Synapse.

---

### **5. Troubleshooting**

| **Issue**                                | **Solution**                                                      |
|------------------------------------------|--------------------------------------------------------------------|
| Query fails with access errors           | Ensure Synapse has permissions to access the Data Lake storage.   |
| Dataset not found in OPENROWSET          | Verify the file path and container name in the query.             |
| Large datasets are slow to query         | Use **Parquet** format instead of CSV for better performance.     |

---

### **6. Deliverable**
Users should:
1. Share the SQL query used to analyze the dataset.
2. Provide a screenshot of the query results in Synapse Studio.

---

### **7. Learning Outcomes**
Users will:
- Understand how to set up and use **Serverless SQL Pools** in Synapse.
- Learn to query raw data stored in a **Data Lake**.
- Perform basic data analysis using SQL.
- Gain hands-on experience with serverless, schema-on-read querying.

---

This project provides a solid foundation for working with **Synapse Analytics** and **Serverless SQL Pools**. Let me know if you'd like further refinements or more advanced examples!