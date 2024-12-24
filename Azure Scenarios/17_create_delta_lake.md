### **Scenario: Setting up and working with Delta Lake on Azure Databricks**

### 1. Objective
- Understand Delta Lake and its benefits.
- Create a Databricks workspace on Azure.
- Configure Delta Lake within Databricks.
- Perform basic operations with Delta Lake.

### 2. Prerequisites
- An **Azure for Students** account with $100 free credits or a standard Azure account.
- Familiarity with Python and basic SQL concepts.

### 3. Key Concepts
- **Delta Lake**: An open-source storage layer that provides ACID transactions and is optimized for large-scale data lakes.
- **Azure Databricks**: A cloud platform for big data analytics and machine learning, providing a collaborative environment for working with large datasets.

### 4. Steps to Create and Configure Delta Lake on Databricks

#### Step 1: Create a Databricks Workspace
1. **Log into Azure Portal**: Go to [Azure Portal](https://portal.azure.com).
2. **Create a Resource Group**: Navigate to "Resource Groups" and create a new one (e.g., `delta-lake-project`).
3. **Create a Databricks Workspace**: Go to "Databricks", create a new workspace with the following:
   - Resource Group: Select the one created earlier.
   - Workspace Name: Choose a name (e.g., `delta-lake-workspace`).
   - Region: Same region as the resource group.
   - Pricing Tier: Choose Standard or Premium.
4. **Launch the Workspace**: After deployment, click "Launch Workspace" to access the Databricks interface.

#### Step 2: Create and Configure a Cluster
1. **Navigate to Clusters Tab**: In Databricks, go to the Clusters section.
2. **Create a Cluster**: Click "Create Cluster" and configure the cluster with:
   - Cluster Name: (e.g., `delta-lake-cluster`).
   - Runtime Version: Choose Databricks Runtime 13.0 or later.
   - Worker Type: Standard_DS3_v2 (or the free tier equivalent).
3. **Create the Cluster**: Wait for the cluster to start.

#### Step 3: Upload Data
1. **Go to the Data Tab**: Click "Data" in the sidebar.
2. **Upload a Dataset**: Upload a CSV file (e.g., `sales_data.csv`) using the "Create Table > Upload File" option.

#### Step 4: Write Data to a Delta Table
1. **Create a Notebook**: Go to "Workspace", create a new notebook (e.g., `DeltaLakeDemo`), and select Python as the language.
2. **Write Code**: In the notebook, use the following code to load data into a Delta table:

   ```python
   from pyspark.sql import SparkSession

   # Create a Spark session
   spark = SparkSession.builder.appName("DeltaLakeDemo").getOrCreate()

   # Load the CSV data
   df = spark.read.format("csv").option("header", "true").load("/FileStore/tables/sales_data.csv")

   # Write data to Delta Table
   delta_table_path = "/mnt/delta/sales_delta"
   df.write.format("delta").mode("overwrite").save(delta_table_path)
   print("Data written to Delta Table")
   ```

3. **Run the Notebook**: Attach the notebook to the cluster and run the cells.

#### Step 5: Query Delta Table
1. **Create the Delta Table**: Add the following code to register the Delta table:

   ```python
   spark.sql(f"CREATE TABLE IF NOT EXISTS sales USING DELTA LOCATION '{delta_table_path}'")
   ```

2. **Query the Data**: Execute a query to view the data:

   ```python
   result = spark.sql("SELECT * FROM sales LIMIT 10")
   result.show()
   ```

#### Step 6: Time Travel in Delta Lake
1. **Add New Data**: Insert new data into the Delta table:

   ```python
   new_data = [("2024-01-01", 5000, "Electronics")]
   columns = ["date", "sales", "category"]
   new_df = spark.createDataFrame(new_data, columns)
   new_df.write.format("delta").mode("append").save(delta_table_path)
   ```

2. **Query Older Versions**: Use time travel to view previous versions:

   ```python
   old_version = spark.sql("SELECT * FROM sales VERSION AS OF 0")
   old_version.show()
   ```

### 5. Troubleshooting
- **Cluster not starting**: Check Azure subscription limits.
- **Unable to access the notebook**: Ensure the notebook is attached to a running cluster.
- **File not found error**: Verify the file path in the code.
- **Schema mismatch error**: Check column types in your data.

### 6. Deliverable
- Screenshot of the Delta table query result.
- Python notebook file (.dbc) with all executed steps.

### 7. Learning Outcomes
- Understand Delta Lake's role in modern data pipelines.
- Gain hands-on experience with Databricks and Delta Lake.
- Learn to manage and query large datasets with ACID guarantees.