### **Scenario 8: Create a Data Dashboard with Power BI Using Azure Data**

This scenario introduces users to creating a live, interactive dashboard in **Power BI** by connecting it to Azure data sources like **Azure SQL Database** or **Azure Synapse Analytics**. Users will query data, visualize insights, and publish a dashboard.

---

### **1. Objective**
Users will:
1. Connect Power BI to an Azure data source (e.g., SQL Database or Synapse Analytics).
2. Create visualizations based on queried data.
3. Publish a Power BI dashboard for sharing and collaboration.

---

### **2. Prerequisites**
1. **Azure for Students account** with $100 free credits.
2. A dataset stored in:
   - **Azure SQL Database** or
   - **Synapse Analytics Serverless SQL Pool**.
3. Installed **Power BI Desktop** (download from [Power BI Desktop](https://powerbi.microsoft.com/desktop/)).

---

### **3. Steps**

#### **Step 1: Prepare the Data in Azure**

##### **Option A: Use Azure SQL Database**
1. **Log in to Azure Portal**:
   - Navigate to your Azure SQL Database.
2. **Set Up a Table**:
   - Open a query editor (e.g., Azure Data Studio) and run the following SQL script to create and populate a table:
     ```sql
     CREATE TABLE SalesData (
         Region NVARCHAR(50),
         Product NVARCHAR(50),
         SalesAmount FLOAT,
         SalesDate DATE
     );

     INSERT INTO SalesData VALUES
     ('North', 'Product A', 1000, '2024-01-01'),
     ('South', 'Product B', 1200, '2024-01-02'),
     ('East', 'Product A', 900, '2024-01-03'),
     ('West', 'Product C', 1500, '2024-01-04');
     ```
3. **Allow External Access**:
   - Enable **Firewall Rules** for the SQL Server to allow your IP or Azure services.

##### **Option B: Use Synapse Analytics Serverless SQL Pool**
1. Query an existing dataset in a **data lake** using **Synapse SQL Pool**:
   ```sql
   SELECT *
   FROM OPENROWSET(
       BULK 'https://<your_storage_account>.dfs.core.windows.net/<container>/salesdata.csv',
       FORMAT = 'CSV',
       PARSER_VERSION = '2.0'
   ) AS [result];
   ```
2. Save the query results for use in Power BI.

---

#### **Step 2: Connect Power BI to Azure**

1. **Open Power BI Desktop**:
   - Launch Power BI Desktop.

2. **Get Data**:
   - Click **Get Data** > **Azure** > Select your data source:
     - For SQL Database: Choose **Azure SQL Database**.
     - For Synapse: Choose **Azure Synapse Analytics**.

3. **Connect to the Data Source**:
   - Enter the server name and database name.
   - Authenticate using **Azure Active Directory** or SQL credentials.

4. **Load Data**:
   - Select the table or view (e.g., `SalesData`) and click **Load**.

---

#### **Step 3: Create Visualizations**

1. **Choose Visualization Types**:
   - Drag and drop fields into the visualization area.
   - Example visualizations:
     - **Bar Chart**: Sales by region.
     - **Pie Chart**: Sales distribution by product.
     - **Line Chart**: Sales trends over time.

2. **Customize Visualizations**:
   - Add titles, labels, and formatting for better readability.

3. **Combine Visuals into a Dashboard**:
   - Arrange the visualizations on a single canvas for a cohesive dashboard.

---

#### **Step 4: Publish the Dashboard**

1. **Save the Power BI Report**:
   - Save your report locally.

2. **Publish to Power BI Service**:
   - Click **Publish** and log in with your Microsoft account.
   - Select a workspace in Power BI Service to upload the report.

3. **Access the Dashboard Online**:
   - Go to [Power BI Service](https://app.powerbi.com).
   - Open the published report and pin visuals to a new dashboard.

4. **Share the Dashboard**:
   - Share the dashboard with others by granting access or creating a public link.

---

### **4. Optional Enhancements**

#### **Add Real-Time Data**:
- Stream live data from **Event Hubs** or **IoT Hub** into Power BI using **Stream Analytics**.

#### **Advanced Visualizations**:
- Add drill-through pages for deeper insights into specific metrics.
- Use custom visuals from the Power BI marketplace.

#### **Dynamic Filters**:
- Add slicers and filters to allow users to explore data interactively.

#### **Integrate with Azure Machine Learning**:
- Use Power BI to display predictions generated by Azure ML.

---

### **5. Troubleshooting**

| **Issue**                                | **Solution**                                                      |
|------------------------------------------|--------------------------------------------------------------------|
| Cannot connect to Azure SQL Database     | Verify firewall rules and authentication credentials.             |
| Data not loading in Power BI             | Check table permissions or query performance in the database.     |
| Visualizations are slow                  | Optimize SQL queries or reduce the data volume.                   |
| Unable to publish report                 | Ensure Power BI Service account is active and properly set up.    |

---

### **6. Deliverable**
Users should:
1. Share the **Power BI Dashboard link**.
2. Provide screenshots of key visualizations (e.g., bar charts, pie charts).

---

### **7. Learning Outcomes**
Users will:
- Understand how to connect Power BI to Azure data sources.
- Learn to create interactive visualizations and dashboards.
- Gain experience publishing and sharing insights through Power BI.
- Explore live data analysis and business intelligence workflows.

---

This project equips users with skills to create dynamic dashboards using **Power BI** and **Azure data sources**, a critical skill for data analytics and business intelligence. Let me know if you'd like further refinements or enhancements!