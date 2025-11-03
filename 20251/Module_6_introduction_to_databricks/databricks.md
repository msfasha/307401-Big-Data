## L1 - Introduction to the Lakehouse Paradigm

**Module:** 1: Databricks and Spark Fundamentals

---

### I. The Challenge of Big Data

#### A. Defining Big Data
* **Volume:** Data size exceeds traditional database processing capabilities (Terabytes to Petabytes).
* **Velocity:** Data is generated rapidly and needs fast processing (real-time or near real-time streams).
* **Variety:** Data comes from diverse sources and formats (structured, semi-structured, unstructured).

#### B. The Need for Distributed Computing
* Traditional Single-Node (vertical scaling) databases hit physical limits.
* Solution: **Horizontal Scaling**—distributing data and processing across a cluster of commodity machines.
* **Apache Hadoop** introduced the concept of distributed storage (HDFS) and processing (MapReduce).
---

### II. Apache Spark: The Next-Generation Engine 
#### A. Limitations of MapReduce
* MapReduce was slow due to extensive disk I/O between processing steps.

#### B. Introducing Apache Spark
* **Speed:** Spark achieves performance gains by performing most computations **in-memory**.
* **Unified Engine:** It provides a single API for batch processing, stream processing, SQL, machine learning, and graph processing.
* **Language Support:** Primary APIs in Scala, Python (PySpark), Java, and R.
---

### III. Evolution of Data Architecture 
#### A. Traditional Data Warehouse (DW)
* **Focus:** Structured, clean data, optimized for reporting and business intelligence (BI).
* **Structure:** Schema-on-Write (data must conform to a schema before loading).
* **Problem:** Expensive, inflexible, and cannot handle raw, unstructured data or machine learning workloads efficiently.

#### B. The Data Lake
* **Focus:** Storing **all** data (raw, structured, unstructured) inexpensively, usually on cloud storage (S3, ADLS, GCS).
* **Structure:** Schema-on-Read (schema is applied when the data is read).
* **Problem:** Lacks data quality, governance, and transactional support (no reliable updates/deletes). This leads to a "Data Swamp."

#### C. The Lakehouse Paradigm
* **Definition:** A new, open data management architecture that combines the best of both Data Warehouses and Data Lakes.
* **Key Enabler:** **Delta Lake** (built on top of the data lake).
* **Advantages:**
    * **Data Warehouse features:** ACID transactions, data governance (Unity Catalog), and high performance.
    * **Data Lake features:** Open formats, low-cost storage, and support for all data types (ML, AI).
---

### IV. Introduction to the Databricks Platform 
#### A. Databricks: The Unified Analytics Platform
* Databricks is the commercial platform built by the creators of Apache Spark, Delta Lake, and MLflow.
* It provides a unified environment to run data engineering, data science, and machine learning workloads.

#### B. Platform Architecture
1.  **Control Plane:**
    * Managed by Databricks (metadata, notebooks, job scheduler, security policies).
    * This is the brain of the platform.
2.  **Data Plane (Compute):**
    * Runs in **your** cloud account (AWS, Azure, GCP).
    * Contains the **Spark Clusters** that process the data.
3.  **Cloud Storage:**
    * Where your data resides (e.g., S3, ADLS). The data always stays in your cloud account.

#### C. Core Components Overview
* **Workspace:** The web interface for collaboration, development, and deployment (where notebooks live).
* **Notebooks:** Interactive web-based environment for writing code (Python, SQL, Scala, R).
* **Clusters:** The compute resources that execute the code on the data plane.
* **Delta Lake:** The core storage layer providing reliability and performance.
---

### V. Summary and Next Steps (5 min)

* We established why distributed computing is necessary for Big Data.
* Spark provides a fast, unified engine for various workloads.
* The Lakehouse Architecture, powered by Databricks, solves the trade-offs between Data Warehouses and Data Lakes.
* **Next Lecture (L2):** We will dive into the practical aspects of setting up and managing the **Databricks Workspace and Clusters**.
## L2 - Databricks Workspace and Cluster Management


**Module:** 1: Databricks and Spark Fundamentals

---

### I. The Databricks Workspace 
The Workspace is the primary **Software as a Service (SaaS)** environment for all development activities.

#### A. Core Components
* **Workspace Browser:** The file system where all assets are stored (notebooks, libraries, experiments, folders).
* **Notebooks:** The central tool for interactive development. They support mixed-language code execution (e.g., mixing Python, SQL, and Scala within one notebook).
* **Repos:** Integration with Git (GitHub, GitLab, Bitbucket, Azure DevOps) to enable **version control** and collaborative development. This is crucial for production-grade data engineering.
* **Jobs:** The place to define, schedule, and monitor non-interactive, production ETL/ELT workflows.

#### B. Magic Commands
* Notebooks use **magic commands** to switch languages within a cell.
    * `%python`: Default language if set to Python.
    * `%sql`: Executes the cell content as SQL.
    * `%scala`: Executes the cell content as Scala.
    * `%r`: Executes the cell content as R.
    * `%run /path/to/notebook`: Executes an entire notebook from within the current one (useful for modularization).

### II. The Databricks Cluster: Compute in the Data Plane 
A cluster is a set of computation resources that provides the platform for running Big Data workloads.

#### A. Key Cluster Components
1.  **Driver Node:**
    * Coordinates the execution of the entire job.
    * Maintains the **SparkContext**, the entry point to Spark functionality.
    * Runs the code for non-distributed operations (e.g., `collect()`).
2.  **Worker Nodes (Executors):**
    * Perform the actual distributed computation and data storage.
    * Communicate with the Driver and with each other.

#### B. Cluster Modes and Types
1.  **All-Purpose Clusters (Interactive):**
    * Used for **interactive development, exploration, and experimentation** via notebooks.
    * Can be shared by multiple users simultaneously.
    * Have a configurable **auto-termination** time to save costs when idle.
2.  **Job Clusters (Automated):**
    * Created automatically by the Databricks Jobs scheduler to run a **specific, single job**.
    * Terminate immediately after the job is finished.
    * More **cost-effective** for production workloads than All-Purpose clusters.
3.  **Single Node Clusters:**
    * Used for non-distributed workloads, development, or testing on smaller datasets.

#### C. Databricks Runtime (DBR)
* The set of core components that run on your clusters.
* Includes Apache Spark, Delta Lake, and various pre-installed libraries (e.g., machine learning frameworks).
* Databricks provides highly optimized, performance-tuned versions of Spark.

### III. Cluster Configuration Decisions 
Optimally configuring a cluster is critical for balancing performance and cost.

#### A. Key Configuration Parameters
1.  **Worker Type and Size (Instance Type):** Determines the CPU, memory, and storage available on each worker node. Choose based on workload (e.g., Memory-Optimized for heavy joins, Compute-Optimized for complex transformations).
2.  **Number of Workers (Scaling):**
    * **Fixed Size:** A set number of workers.
    * **Autoscaling:** Automatically adjusts the number of workers within a specified minimum and maximum range based on the workload queue. Recommended for variable workloads.
3.  **Databricks Units (DBUs):** The unit of processing capacity consumed by Databricks, used for billing. Understanding DBU consumption is key to cost management.

#### B. Managing External Libraries
* Libraries (e.g., Python packages like `requests`, `pandas`) must be installed on the cluster, not just locally in the notebook.
* Databricks supports installing libraries via PyPI, Maven, or uploading JAR/whl files directly.

### IV. Data Access Fundamentals (5 min)

Before processing data, the cluster must be able to reach it.

* **DBFS (Databricks File System):** A distributed file system mounted on the Databricks cluster. It's used for temporary storage and mounted access to external cloud storage.
* **External Data Access:** Typically involves configuring credentials (e.g., Service Principals in Azure, IAM roles in AWS) to allow the Databricks compute plane to securely read and write data in the cloud storage layer.

### V. Summary and Next Steps (5 min)

* The **Workspace** is the collaborative IDE for development and deployment.
* **Clusters** are the dynamic compute engines, with **All-Purpose** for dev and **Job Clusters** for production.
* Effective configuration of worker size and autoscaling saves both time and money.
* **Next Lecture (L3):** We will dive into the core engine—the **Apache Spark Architecture**—to understand how it achieves its speed and distributed capabilities.
## L3 - Apache Spark Architecture Explained


**Module:** 1: Databricks and Spark Fundamentals

---

### I. The Core Components of a Spark Cluster 
Spark operates as a distributed system, relying on several key processes to coordinate work across a cluster.

#### A. The Driver Program and SparkContext
* **Driver Program:** Runs the main method of your application (the notebook code). It is responsible for creating and coordinating all other cluster components.
* **SparkContext:** The entry point to all Spark functionality. When you run a Spark application, the Driver creates a SparkContext, which connects to the Cluster Manager.
* **Role:** The Driver analyzes your code, creates a logical plan (DAG), and transforms it into a physical plan for execution.

#### B. The Cluster Manager
* **Role:** Manages the resources of the cluster (e.g., EC2 instances, Azure VMs). It acquires executor resources on behalf of the application.
* **Examples:** **Databricks** uses an optimized internal cluster manager, but Spark can also work with standalone mode, YARN, or Mesos.

#### C. The Executor (Worker) Nodes
* **Role:** These are the workers that perform the heavy lifting. They execute the tasks assigned by the Driver, store data in memory or on disk, and report results back to the Driver.
* **Task:** The smallest unit of work in Spark. A job is broken down into stages, and each stage is composed of tasks.

---

### II. Data Abstractions and Structure 
Spark evolved its core data structures to improve both usability and performance.

#### A. Resilient Distributed Datasets (RDDs)
* **Definition:** The fundamental, low-level data structure in Spark. An RDD is an immutable, partitioned collection of elements that can be operated on in parallel.
* **Resilient:** It can automatically recover from failures on worker nodes.
* **Distributed:** Data is spread across the worker nodes.
* **Limitation:** RDDs are schema-less, making them less efficient for complex queries and optimization. They are rarely used directly today, but remain the underlying engine.

#### B. DataFrames (The Standard)
* **Definition:** A distributed collection of data organized into named columns, conceptually equivalent to a table in a relational database.
* **Advantage:** Unlike RDDs, DataFrames have a **schema**, allowing for significant performance optimizations.

---

### III. The Execution Flow: Lazy Evaluation and Optimization 
Spark's execution model is what makes it fast and flexible.

#### A. Lazy Evaluation
* **Principle:** Spark does **not** execute transformations immediately when they are called. Instead, it builds up a plan (a **Directed Acyclic Graph or DAG**).
* **Benefit:** This allows Spark to look at the entire sequence of operations before executing anything. It can then optimize the whole pipeline, avoiding unnecessary steps and intermediate results.

#### B. Transformations vs. Actions
* **Transformations:** Operations that return a new DataFrame but are executed **lazily**.
    * **Example:** `select()`, `filter()`, `groupBy()`.
* **Actions:** Operations that trigger the execution of the entire DAG and return a result to the Driver or write to an external sink.
    * **Example:** `show()`, `count()`, `write()`, `collect()`.

#### C. The Catalyst Optimizer
* **Role:** Spark's core optimization engine. It takes the logical plan (the DAG from your code) and uses a set of rules to transform it into the most efficient physical execution plan.
* **Phases:** Analysis (resolving column names), Logical Optimization (predicate pushdown), Physical Planning, and Code Generation.

---

### IV. Wide vs. Narrow Transformations 
Understanding the network cost of a transformation is crucial for performance.

#### A. Narrow Transformations
* **Definition:** Operations where all required input data to compute a result is already on the same partition (i.e., on the same worker node).
* **Cost:** **Low Network Cost**. No data needs to be moved between nodes.
* **Examples:** `filter()`, `select()`, `withColumn()`.

#### B. Wide Transformations
* **Definition:** Operations that require data to be moved or exchanged across the cluster partitions (nodes). This process is called a **Shuffle**.
* **Cost:** **High Network Cost** (I/O, serialization, network latency). Shuffles are often the biggest performance bottleneck.
* **Examples:** `groupBy()`, `join()`, `repartition()`, `orderBy()`.

---

### V. Summary and Next Steps (5 min)

* Spark execution is coordinated by the **Driver**, managed by the **Cluster Manager**, and executed by the **Executors**.
* **DataFrames** (with schemas) are the foundation for efficient processing.
* **Lazy Evaluation** combined with the **Catalyst Optimizer** ensures code runs efficiently.
* **Shuffles (Wide Transformations)** are costly and should be minimized or optimized.
* **Next Lecture (L4):** We will start writing actual code, focusing on the Spark DataFrame API and fundamental concepts.
## L4 - Introduction to Spark DataFrames


**Module:** 1: Databricks and Spark Fundamentals

-----

### I. DataFrames: The Workhorse of Modern Spark 
#### A. Why DataFrames?

  * **Structured Data:** Unlike RDDs, DataFrames organize data into named columns, just like a table in a relational database or a sheet in a spreadsheet.
  * **Optimization:** The presence of a **schema** allows the **Catalyst Optimizer** to perform massive performance improvements (e.g., column pruning, predicate pushdown).
  * **Usability:** Provides a rich, high-level, and intuitive API (similar to Pandas or R DataFrames), making code easier to write and read.

#### B. The SparkSession

  * The **SparkSession** is the unified entry point to all of Spark's features (including DataFrames, SQL, and Streaming).
  * In Databricks notebooks, the SparkSession is automatically created for you as the variable `spark`. You generally don't need to manually create it.

### II. Creating DataFrames 
There are three primary ways to create a DataFrame:

#### A. From Existing Data Sources (Most Common)

  * Use `spark.read` along with a format method. This is how you read Big Data.

| Format | Example (PySpark) | Notes |
| :--- | :--- | :--- |
| **Parquet** | `df = spark.read.parquet("/mnt/data/sales.parquet")` | Default and recommended format for its speed and compression. |
| **CSV** | `df = spark.read.option("header", "true").csv("/mnt/data/users.csv")` | Requires options for header and schema inference. |
| **JSON** | `df = spark.read.json("/mnt/data/logs.json")` | Used for semi-structured data. |

#### B. From an Existing RDD (Less Common)

  * DataFrames can be created by converting an RDD, often used when integrating legacy Spark code.

#### C. From Local Data (Small Datasets for Testing)

  * Use the `createDataFrame` method to create a DataFrame from local lists or tuples.

<!-- end list -->

```python
# Example for creating a small DataFrame
data = [("Alice", 1), ("Bob", 2)]
columns = ["name", "id"]
test_df = spark.createDataFrame(data, columns)
test_df.show() 
```

### III. Schema and Data Types 
#### A. What is a Schema?

  * The blueprint of the DataFrame, defining the column names and their associated data types.

#### B. Schema Inference vs. Explicit Schema

  * **Inference:** When reading a file (like CSV), Spark can try to **infer** the schema by sampling the data. This is convenient but slow and can lead to errors with inconsistent data.
  * **Explicit (Best Practice):** Define the schema explicitly using `StructType` and `StructField`. This is faster, more robust, and ensures data quality.

<!-- end list -->

```python
# Example of explicit schema definition
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

user_schema = StructType([
    StructField("user_id", IntegerType(), True),
    StructField("username", StringType(), False) # False means non-nullable
])

# Use the schema when reading the file
# df = spark.read.schema(user_schema).json("/data.json") 
```

### IV. Basic DataFrame Interaction 
#### A. Inspection

  * **`printSchema()`:** Displays the schema in a tree format (column name and data type). Essential for debugging.
  * **`show()`:** Displays the first few rows of the DataFrame (triggers an Action).
  * **`display(df)` (Databricks Feature):** A Databricks-specific command that formats the data into a rich, scrollable HTML table and allows quick visualization creation.

#### B. Columns and Selection

  * You can refer to columns using string names or the `col()` function.
  * **`df.select("colA", "colB")`:** Selects specified columns.
  * **`df.colA` or `df["colA"]`:** Shorthand ways to reference a column object.

### V. Summary and Next Steps (5 min)

  * **DataFrames** are structured, schema-aware, and highly optimized by the Catalyst Optimizer.
  * The **SparkSession (`spark`)** is your starting point.
  * The best way to load data is using **`spark.read.<format>()`**.
  * **Explicit Schemas** are the recommended best practice for reliability and speed.
  * **Next Lecture (L5):** We will explore the core concepts of **Transformations and Actions**, which are the building blocks of every Spark data pipeline.
  ## L5 - Working with Data: Transformations and Actions


**Module:** 1: Databricks and Spark Fundamentals

-----

### I. The Core Dichotomy: Transformations vs. Actions 
The fundamental concept in Spark is understanding how operations are executed: lazily (Transformations) versus immediately (Actions).

#### A. Transformations

  * **Definition:** Operations performed on a DataFrame that produce a **new DataFrame**.
  * **Execution:** They are executed **lazily**. Calling a transformation simply records the operation in the DAG (Directed Acyclic Graph) execution plan; no data processing occurs yet.
  * **Goal:** To define the sequence of data manipulation steps.
  * **Types:** Transformations can be **Narrow** (no shuffle) or **Wide** (involving a shuffle), as discussed in L3.

#### B. Actions

  * **Definition:** Operations that trigger the execution of all preceding, chained transformations in the DAG.
  * **Execution:** They are executed **eagerly** (immediately). They initiate the movement of tasks to the cluster's Executors.
  * **Goal:** To materialize a result, either by returning data to the Driver or by writing data to a storage system.

| Feature | Transformation | Action |
| :--- | :--- | :--- |
| **Output** | New DataFrame (Pointer) | Local Value or Write to Storage |
| **Execution** | Lazy (builds the plan) | Eager (triggers execution) |
| **Examples** | `select()`, `filter()`, `withColumn()`, `groupBy()` | `show()`, `count()`, `collect()`, `write()`, `toPandas()` |

-----

### II. Essential Transformations 
These are the building blocks of any ETL (Extract, Transform, Load) process.

#### A. Filtering and Selection

  * **`filter()` or `where()` (Narrow):** Selects rows based on a given condition.
    ```python
    # Filter for orders over 100
    large_orders_df = orders_df.filter(orders_df["amount"] > 100)
    ```
  * **`select()` (Narrow):** Selects a set of columns.
    ```python
    # Select only the ID and Amount columns
    reduced_df = orders_df.select("order_id", "amount")
    ```

#### B. Adding and Dropping Columns

  * **`withColumn()` (Narrow):** Adds a new column or replaces an existing one. Requires an expression or a new value.
    ```python
    # Add a new tax column
    taxed_df = orders_df.withColumn("tax", orders_df["amount"] * 0.05)
    ```
  * **`drop()` (Narrow):** Removes one or more columns from the DataFrame.
    ```python
    clean_df = taxed_df.drop("order_id")
    ```

#### C. Renaming and Casting

  * **`withColumnRenamed()` (Narrow):** Renames a single column.
    ```python
    renamed_df = clean_df.withColumnRenamed("amount", "total_price")
    ```
  * **`cast()` (Narrow):** Changes the data type of a column (e.g., String to Integer).
    ```python
    from pyspark.sql.types import IntegerType
    casted_df = orders_df.withColumn("order_id", orders_df["order_id"].cast(IntegerType()))
    ```

-----

### III. Essential Actions 
Actions are how you inspect or persist your results.

#### A. Data Inspection

  * **`show(n)`:** Displays the first `n` rows of the DataFrame to the console. The most common action for development.
  * **`count()`:** Returns the total number of rows in the DataFrame as a single value (an Action that triggers a full scan).
  * **`collect()`:** Returns **all** the data from the DataFrame to the Driver program as a Python list of `Row` objects. **Caution:** Use only on small DataFrames to prevent the Driver from running out of memory.

#### B. Writing Data

  * **`write`:** The action used to persist the DataFrame data to a file system or database.
    ```python
    # Example: Writing the result to a Delta table
    final_df.write.format("delta").mode("overwrite").save("/mnt/processed/final_data")
    ```
      * **`format()`:** Specifies the output file format (e.g., `parquet`, `csv`, `delta`).
      * **`mode()`:** Defines how to handle existing data (`overwrite`, `append`, `ignore`, `errorifexists`).

-----

### IV. Practical Example: Chaining Operations (5 min)

The power of Spark comes from chaining transformations together, with the Action triggering the efficient execution.

```python
# Chaining an ETL process
final_df = (
    # 1. Start with the source data
    spark.read.parquet("/data/raw_sales")
    # 2. Transformation: Add a new calculated column
    .withColumn("is_expensive", col("price") > 500)
    # 3. Transformation: Filter out low-value orders
    .filter(col("quantity") > 1)
    # 4. Transformation: Select the final columns
    .select("product_id", "is_expensive", "quantity")
)

# 5. Action: Persist the final, clean data
final_df.write.format("delta").mode("append").save("/data/gold_layer")

# 6. Action: Quick check of the first 5 rows
final_df.show(5)
```

The Spark engine executes steps 1-5 in an optimized sequence only after the `write` and `show` actions are called.

-----

### V. Summary and Next Steps (5 min)

  * **Transformations** build the DAG execution plan lazily; **Actions** trigger it eagerly.
  * Key Transformations: `select()`, `filter()`, `withColumn()`, `drop()`.
  * Key Actions: `show()`, `count()`, `write()`.
  * **Caution:** Be extremely careful with the `collect()` Action on large datasets.
  * **Next Lecture (L6):** We will focus entirely on **Data Ingestion and Sources**, learning how to efficiently read and write Big Data from various file formats and cloud locations.

  ## L6 - Data Ingestion and Sources


**Module:** 2: Core Data Processing

-----

### I. The Data Ingestion Workflow 
Data ingestion is the crucial first step: moving data from its source into the environment where Spark can process it.

#### A. Spark's `spark.read` Interface

  * The `spark.read` object is the entry point for reading data into a DataFrame.
  * It uses a builder pattern: you specify options, the format, and the location.

<!-- end list -->

```python
# General read pattern
df = spark.read.option("<key>", "<value>").format("<format>").load("<path>")
```

#### B. The Need for Distributed Storage

  * Spark doesn't store the data; it processes it. Data must reside on a **distributed file system** or object store that all worker nodes can access.
      * **Cloud Object Stores:** AWS S3, Azure Data Lake Storage (ADLS Gen2), Google Cloud Storage (GCS). This is the standard for the Lakehouse.
      * **DBFS (Databricks File System):** An abstraction layer that simplifies interaction with these cloud stores and provides local-like access points.

### II. Working with Common File Formats 
The choice of file format significantly impacts ingestion speed and query performance.

#### A. Row-Oriented Formats (e.g., CSV, JSON)

  * **CSV (Comma-Separated Values):** Simple, human-readable, but lacks standardization (e.g., header, quoting issues).
      * **Ingestion:** Requires options like `.option("header", "true")` and `.option("inferSchema", "true")` (use sparingly).
  * **JSON (JavaScript Object Notation):** Good for semi-structured data, handles nested fields.
      * **Challenge:** Spark reads the entire line for each record, which can be slow, and schema inference is required for structure.

#### B. Columnar-Oriented Formats (e.g., Parquet, ORC)

  * **Parquet (Highly Recommended):** The industry standard for Big Data analytics.
      * **Columnar Storage:** Stores data column-by-column, allowing Spark to read **only the necessary columns** for a query (**Columnar Pruning**).
      * **Compression:** Highly compressed and optimized for query performance.
      * **Schema:** Stores the schema and metadata *with* the data, making it fast to read.
  * **ORC (Optimized Row Columnar):** Similar benefits to Parquet, often used in older Hadoop ecosystems.

**Takeaway:** Always convert raw data (CSV, JSON) into **Parquet** or **Delta Lake** (covered later) as early as possible in the pipeline.

### III. Accessing Data in Databricks 
Databricks provides multiple ways to reference and access data securely.

#### A. DBFS Paths (`dbfs:/`)

  * **Role:** DBFS is a virtual file system that mounts cloud storage locations and provides access to local storage on the cluster nodes.
  * **Paths:** Use the `dbfs:/` prefix to refer to files.
  * **Use Cases:** Simple file staging, access to utility files. *Note: DBFS should not be considered a primary, persistent data warehouse.*

#### B. Mount Points (Legacy but useful)

  * A configuration that securely maps a path in your cloud storage (e.g., `s3://bucket-name/folder`) to a local-looking path (e.g., `/mnt/data`).
  * **Security:** Credentials (keys/roles) are stored securely in Databricks secrets, not in the notebook code.

#### C. Direct Cloud Access (Modern & Preferred)

  * Directly accessing cloud paths (e.g., `s3a://...` or `abfss://...`) configured via the cluster's IAM roles or service principals. This is generally the most secure and scalable approach as it leverages the cloud platform's built-in access controls.

### IV. Writing DataFrames (5 min)

The `df.write` object is the counterpart to `spark.read`.

  * **The `mode()` Option:** Crucial for controlling write behavior:

      * **`overwrite`:** Deletes existing data at the path and writes the new DataFrame.
      * **`append`:** Adds the new records to the existing data.
      * **`errorifexists` (default):** Throws an error if data already exists at the path.
      * **`ignore`:** Does nothing if data already exists.

  * **Partitioning the Data:**

      * Using `.partitionBy("column_name")` organizes the output files into subdirectories based on column values (e.g., `/data/year=2024/month=01`).
      * **Benefit:** Speeds up queries that filter on the partitioning column. **Caution:** Avoid partitioning on high-cardinality columns (too many small files).

### V. Summary and Next Steps (5 min)

  * Use the `spark.read` and `df.write` interfaces for all ingestion and persistence.
  * **Parquet** is the preferred format for analytics due to its columnar nature.
  * Data ingestion is all about securely pointing Spark Compute to your data in Cloud Storage.
  * **Next Lecture (L7):** We will move beyond basic filters and explore **Advanced Data Manipulation** using functions, expressions, grouping, and aggregation.

  ## L7 - Advanced Data Manipulation


**Module:** 2: Core Data Processing

-----

### I. The Spark SQL Functions Library 
While basic filtering and selecting are simple, complex data cleaning and transformation require a powerful set of functions. Spark provides an extensive library of built-in functions via `pyspark.sql.functions`.

#### A. Importing and Referencing Functions

  * You must explicitly import the functions you need. The convention is to import them as `F`.

<!-- end list -->

```python
from pyspark.sql import functions as F
from pyspark.sql.functions import col
```

#### B. Common Function Categories

  * **String Functions:** `F.upper()`, `F.lower()`, `F.trim()`, `F.substring()`, `F.concat()`.
  * **Mathematical Functions:** `F.round()`, `F.ceil()`, `F.floor()`, `F.abs()`.
  * **Date and Time Functions:** `F.current_timestamp()`, `F.date_format()`, `F.year()`, `F.to_date()`.

#### C. Working with Expressions

  * All column operations in Spark should use the `col()` object or a function wrapping it.

<!-- end list -->

```python
# Example: Trimming whitespace and converting to uppercase
df = df.withColumn("Cleaned_Name", F.upper(F.trim(col("Raw_Name"))))
```

-----

### II. Conditional Logic 
Conditionals allow you to apply complex business logic to create new columns or transform existing data.

#### A. The `when().otherwise()` Construct

  * This is Spark's equivalent of a SQL `CASE` statement. It allows for multiple nested conditions.

<!-- end list -->

```python
df = df.withColumn(
    "Category_Group",
    F.when(col("Price") > 1000, F.lit("Premium")) # F.lit() creates a literal value
     .when(col("Price") > 500, F.lit("Standard"))
     .otherwise(F.lit("Economy"))
)
```

#### B. The `F.lit()` Function

  * Used to introduce a **literal value** (a constant, non-column value) into a DataFrame operation, such as the string values in the example above.

-----

### III. Grouping and Aggregation 
Aggregation is a **Wide Transformation** (requires a shuffle) used to summarize data.

#### A. The `groupBy()` and `agg()` Functions

  * **`groupBy()`:** Defines the column(s) by which you want to group the data.
  * **`agg()`:** Applies one or more aggregation functions to the grouped data.

<!-- end list -->

```python
# Aggregate functions like F.sum(), F.avg(), F.max(), F.min(), F.count()
summary_df = sales_df.groupBy("Product_ID", "City").agg(
    F.sum("Revenue").alias("Total_Revenue"),
    F.avg("Units_Sold").alias("Average_Units")
)
summary_df.show()
```

#### B. Multi-Aggregation Syntax

  * You can pass a dictionary of aggregations to the `agg()` function, but the list syntax above is generally preferred for clarity when renaming columns.

#### C. Pivot and Rollup (Advanced Aggregation)

  * **`pivot()`:** Transforms rows into columns, allowing aggregation across a specified pivot column (often involves a significant shuffle).
  * **`rollup()`/`cube()`:** Provides hierarchical totals beyond basic grouping (useful for reporting).

-----

### IV. User-Defined Functions (UDFs) 
UDFs allow you to extend Spark's capabilities by writing custom code in Python or Scala.

#### A. Defining and Registering a UDF

1.  Define a standard Python function.
2.  Import `udf` from `pyspark.sql.functions`.
3.  Register the function, specifying the **return type** (mandatory).

<!-- end list -->

```python
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# 1. Define the custom Python logic
def grade_classifier(score):
    if score >= 90:
        return "A"
    return "Below A"

# 2. Register the UDF with its return type
classify_udf = udf(grade_classifier, StringType())

# 3. Apply the UDF to the DataFrame
students_df = students_df.withColumn("Grade", classify_udf(col("Final_Score")))
```

#### B. Performance Warning: Python UDFs

  * **The Drawback:** When a Python UDF runs, Spark must:
    1.  Serialize the data from the JVM (Scala/Spark) to Python.
    2.  Execute the function in a separate Python process (interpreter).
    3.  Serialize the result back to the JVM.
  * **The Rule:** Python UDFs are very slow and should be avoided whenever a built-in Spark function can achieve the same result. They break the efficiency of the Catalyst Optimizer.
  * **Alternative:** Look into **Vectorized UDFs (Pandas UDFs)** for better performance, but they are an advanced topic for later study.

-----

### V. Summary and Next Steps (5 min)

  * Use the rich **Spark SQL Functions Library (`F`)** for transformations before resorting to custom code.
  * **`when().otherwise()`** is essential for implementing complex conditional logic.
  * **Aggregation** using `groupBy()` and `agg()` is a **Wide Transformation** that summarizes data.
  * **UDFs** provide flexibility but introduce performance overhead due to serialization between the JVM and Python. Use built-in functions whenever possible.
  * **Next Lecture (L8):** We will focus on the most critical Wide Transformations: **Joins and Set Operations**, learning how to efficiently combine large datasets.

  ## L8 - Joins and Set Operations


**Module:** 2: Core Data Processing

-----

### I. Joins in Spark: Combining DataFrames 
Combining two DataFrames is a fundamental operation in ETL, but in Spark, it's a **Wide Transformation** that requires careful handling due to the resource-intensive **Shuffle**.

#### A. The `join()` Syntax

The basic syntax for joining two DataFrames (`df_left` and `df_right`) is:

```python
joined_df = df_left.join(df_right, on="key_column", how="join_type")
```

  * **`on`:** Specifies the column(s) to match. Can be a string, a list of strings, or a complex expression.
  * **`how`:** Specifies the join type.

#### B. Types of Joins

Spark supports the standard SQL join types:

| Join Type (`how` value) | Description | Result |
| :--- | :--- | :--- |
| **`inner`** (Default) | Returns only rows with **matching keys** in both DataFrames. | Intersection of both datasets. |
| **`left_outer`** | Returns all rows from the left DF and the matching rows from the right DF. Non-matching right columns are `null`. | All left rows preserved. |
| **`right_outer`** | Returns all rows from the right DF and the matching rows from the left DF. Non-matching left columns are `null`. | All right rows preserved. |
| **`full_outer`** | Returns all rows when there is a match in either DF. Non-matching columns are `null`. | Union of both datasets. |
| **`left_semi`** | Returns records from the left DF where the join key **exists** in the right DF. *Does not include columns from the right DF.* | Acts as a fast filter. |
| **`left_anti`** | Returns records from the left DF where the join key **does not exist** in the right DF. *Does not include columns from the right DF.* | Acts as an exclusion filter. |

-----

### II. Dealing with Ambiguous Columns (5 min)

When two DataFrames share column names (other than the join key), Spark can't distinguish them.

#### A. Column Name Collisions

If both `df_a` and `df_b` have a column named `timestamp`, the resulting DataFrame will have two `timestamp` columns, leading to ambiguity errors.

#### B. Resolution Strategies

1.  **Aliasing/Renaming:** Rename the conflicting columns *before* the join.
    ```python
    df_b_renamed = df_b.withColumnRenamed("timestamp", "b_timestamp")
    joined_df = df_a.join(df_b_renamed, ...)
    ```
2.  **`select` and `drop` After Join:** If you only need one version of the conflicting column, use `.drop(df_right["conflicting_column"])` after the join.

-----

### III. Join Optimization and Techniques 
Because joins trigger a shuffle (moving data across the network), they are the most common source of performance bottlenecks.

#### A. The Shuffle Problem

When two DataFrames are joined, all rows with the same join key must be moved to the same worker node to be physically matched. This network transfer is slow.

#### B. Broadcast Hash Join (BHJ)

  * **Concept:** If one DataFrame is **small enough** (default threshold is 10MB in Spark config, but often up to hundreds of MB is feasible), Spark will copy that entire DataFrame to the memory of *every* worker node.
  * **Benefit:** Eliminates the costly shuffle for the large DataFrame, as the join can be performed locally on each worker.
  * **Implementation (Hint):** You can explicitly force a broadcast join using the `broadcast()` function.

<!-- end list -->

```python
from pyspark.sql.functions import broadcast

# Tell Spark to broadcast the small_lookup_df
efficient_join = large_df.join(broadcast(small_lookup_df), "key")
```

#### C. Skewed Joins

  * **Problem:** If the join key has a highly uneven distribution (e.g., 90% of your data has `key_id = 1`), one worker node will get 90% of the data.
  * **Result:** That single worker will become a **bottleneck** while others sit idle.
  * **Mitigation:** Skew handling requires advanced techniques like salting (adding random prefixes to the skewed keys), which is beyond this introductory lecture.

-----

### IV. Set Operations 
Set operations combine DataFrames based on their content, not a specific key. They require the two DataFrames to be **schema-compatible** (same number of columns, same column names, same order, and compatible data types).

#### A. `union()` and `unionByName()`

  * **`union()`:** Appends the rows of one DataFrame to another. It combines columns **by position**.
    ```python
    combined_df = df_2023.union(df_2024)
    ```
  * **`unionByName()`:** Appends rows by matching column names, ignoring the order of columns. This is generally safer and preferred for ETL.

#### B. Filtering Set Operations

  * **`intersect()`:** Returns only the rows that appear in **both** DataFrames.
  * **`except()`:** Returns the rows that are in the **first** DataFrame but **not** in the second.

-----

### V. Summary and Next Steps (5 min)

  * **Joins** are **Wide Transformations** that require a shuffle; choose your join type (`how`) carefully.
  * **Broadcast Hash Join (BHJ)** is the most important optimization technique: use it whenever one DataFrame is small.
  * **Set Operations** (`union`, `intersect`, `except`) are used to combine or compare DataFrames based on their row content, requiring strict schema compatibility.
  * **Next Lecture (L9):** We will explore **Window Functions**, a powerful tool for complex analytics that allow you to perform calculations across a defined set of related rows.

  ## L9 - Window Functions for Complex Analytics


**Module:** 2: Core Data Processing

-----

### I. Introduction to Window Functions 
Window functions perform a calculation across a set of table rows that are somehow related to the current row. They are the key to advanced ranking, comparison, and moving calculations in a distributed environment.

#### A. Key Concept: The "Window"

  * A window is a set of rows defined by the user that is related to the row being evaluated.
  * **Crucially:** Unlike `groupBy()`, which collapses rows into a single summary row, a window function **retains the original rows** and simply adds a calculated column to the DataFrame.

#### B. Structure of a Window Function

A window function has three parts:

1.  **Window Function:** The aggregation or ranking function (e.g., `sum()`, `avg()`, `row_number()`).
2.  **Partitioning:** Defines the groups (the "windows") of rows to operate on.
3.  **Ordering and Framing:** Defines the order *within* the partition and the range of rows (the "frame") to include in the calculation.

-----

### II. Defining the Window Specification 
Before applying the function, you must define the window using the `Window` object.

#### A. The `Window` Object

You need to import the `Window` class from `pyspark.sql.window`.

```python
from pyspark.sql.window import Window
from pyspark.sql import functions as F
```

#### B. Partitioning the Data (`partitionBy`)

  * This is similar to the `GROUP BY` clause in SQL, but it *groups* the data without *aggregating* it.
  * A single window calculation is performed independently within each partition.

<!-- end list -->

```python
# Partition data by 'Department'
window_spec = Window.partitionBy("Department")
```

#### C. Ordering the Data (`orderBy`)

  * This specifies the order of rows *within* each partition. This is essential for ranking functions and running totals.

<!-- end list -->

```python
# Order data within each department by 'Salary' in descending order
window_spec = Window.partitionBy("Department").orderBy(F.desc("Salary"))
```

-----

### III. Common Window Functions 
These functions are applied to the defined window specification using the `.over()` clause.

#### A. Ranking Functions

These assign a numerical rank to each row within its partition.

  * **`row_number()`:** Assigns a sequential, unique integer rank (1, 2, 3, 4...).
  * **`rank()`:** Assigns the same rank to ties, leaving gaps in the sequence (1, 2, 2, 4...).
  * **`dense_rank()`:** Assigns the same rank to ties, **without** leaving gaps (1, 2, 2, 3...).

<!-- end list -->

```python
# Find the highest paid employee (Rank 1) in each department
df_ranked = df.withColumn(
    "Dept_Rank",
    F.rank().over(Window.partitionBy("Department").orderBy(F.desc("Salary")))
)
```

#### B. Analytical and Value Functions

These pull data from specific rows in the window.

  * **`lag()` / `lead()`:** Accesses values from a preceding (lag) or succeeding (lead) row. Useful for calculating **period-over-period differences**.
  * **`first()` / `last()`:** Returns the first or last value in the partition (after ordering).

<!-- end list -->

```python
# Calculate the salary difference between the current year and the previous year
df_lagged = df.withColumn(
    "Prev_Year_Salary",
    F.lag(F.col("Salary"), 1).over(Window.partitionBy("Employee_ID").orderBy("Year"))
)
```

-----

### IV. Window Framing (Running Totals) 
Window framing defines the set of rows (the "frame") relative to the current row that the aggregate function should include.

#### A. Default Frame

  * For **ranking** functions, the frame is the entire partition (no need to define the frame).
  * For **aggregate** functions (like `sum` or `avg`), the default is to aggregate the entire partition, which is often not what you want for running totals.

#### B. Running Total Frame

To calculate a cumulative or running total, you define the frame to start at the beginning of the partition and end at the current row.

  * **`rowsBetween(Window.unboundedPreceding, Window.currentRow)`**

<!-- end list -->

```python
# Calculate the Running Total of sales within each store
running_spec = Window.partitionBy("Store_ID").orderBy("Sale_Date").rowsBetween(
    Window.unboundedPreceding, Window.currentRow
)

df_running = df.withColumn(
    "Cumulative_Sales",
    F.sum("Revenue").over(running_spec) # Aggregation function over a running frame
)
```

### V. Summary and Next Steps (5 min)

  * **Window Functions** add calculated columns based on related rows without reducing the number of rows.
  * The **Window Specification** is defined using `partitionBy()` (groups) and `orderBy()` (sequence).
  * **Ranking functions** (`row_number`, `rank`, `dense_rank`) are common for top-N analysis.
  * **Lag/Lead functions** are essential for time-series comparisons.
  * **Window Framing** (using `rowsBetween`) is necessary for calculating running totals and moving averages.
  * **Next Lecture (L10):** We will step back from the DataFrame API and explore **Spark SQL**, learning how to leverage SQL directly for data processing in Databricks.

  ## L10 - Spark SQL


**Module:** 2: Core Data Processing

-----

### I. Spark SQL: Bridging the Gap 
Spark SQL is a module for working with structured data using SQL queries. It's fully integrated with the DataFrame API, allowing you to seamlessly switch between programmatic data manipulation (PySpark) and declarative querying (SQL).

#### A. Why Use Spark SQL?

  * **Familiarity:** Allows SQL experts to leverage Spark's distributed processing power without learning Python or Scala APIs in depth.
  * **Optimization:** SQL queries are analyzed directly by the **Catalyst Optimizer**, often leading to very efficient execution plans (sometimes better than manual API code).
  * **Interoperability:** Easily combine results from SQL queries with DataFrame operations in the same notebook.

#### B. The Databricks Advantage

  * Databricks notebooks allow you to use the **`%sql` magic command** to execute SQL queries directly against your clusters and tables.
  * Results are displayed in rich HTML tables with built-in charting capabilities.

-----

### II. Working with Spark SQL in Databricks 
#### A. The `%sql` Magic Command

In a Databricks notebook cell, simply start the cell with `%sql` to switch the interpreter for that cell.

```sql
%sql
SELECT 
  customer_id, 
  SUM(order_value) AS total_spend
FROM 
  sales.orders
WHERE 
  order_date >= '2025-01-01'
GROUP BY 
  customer_id
ORDER BY 
  total_spend DESC
LIMIT 10;
```

#### B. Tables and Views

SQL queries must operate on a relational structure, which means using persistent tables or temporary views.

1.  **Permanent Tables:** Stored in the Metastore (later: Unity Catalog) and accessible by name across sessions, users, and clusters.
    ```sql
    %sql
    CREATE TABLE sales.customers (
      customer_id INT,
      name STRING,
      city STRING
    ) USING delta; -- Specify the format (Delta is preferred)
    ```
2.  **Temporary Views:** A schema defined for the duration of the current SparkSession (or cluster).
      * **Lifetime:** Only visible within the SparkSession that created it.
      * **Creation from PySpark:** `my_df.createOrReplaceTempView("temp_orders")`

#### C. Global Temporary Views

  * **Creation:** `my_df.createOrReplaceGlobalTempView("global_temp_orders")`
  * **Lifetime:** Visible across **all sessions running on the same cluster**. Must be queried using the special prefix `global_temp.`.
    ```sql
    %sql
    SELECT * FROM global_temp.global_temp_orders;
    ```

-----

### III. Seamless Interoperability 
The ability to pass data between the DataFrame API and Spark SQL is a core strength.

#### A. PySpark to Spark SQL

The most common workflow is to read or process data using the DataFrame API and then expose the result to SQL for analysis or reporting.

1.  **Process with DataFrame API:**
    ```python
    # Read the data using PySpark
    raw_df = spark.read.parquet("/mnt/data/bronze/transactions")
    # Perform complex joins/transformations
    processed_df = raw_df.filter(...) 

    # 2. Expose the result to SQL
    processed_df.createOrReplaceTempView("v_processed_transactions")
    ```
2.  **Query using SQL:**
    ```sql
    %sql
    -- Now query the view created in the PySpark cell
    SELECT transaction_date, SUM(amount) FROM v_processed_transactions GROUP BY 1;
    ```

#### B. Spark SQL to PySpark

You can also execute a SQL query and immediately get the result as a DataFrame object in your programmatic code.

```python
# Use spark.sql() to execute the query
sql_result_df = spark.sql("""
  SELECT name, email
  FROM sales.customers
  WHERE is_active = true
""")

# Continue processing the result using PySpark API
final_output = sql_result_df.withColumn("is_vip", F.lit(True))
final_output.show()
```

-----

### IV. Advanced SQL Features (5 min)

Spark SQL supports a wide range of analytical functions, including those we covered programmatically.

  * **Window Functions:** Directly use standard SQL syntax for windowing (`PARTITION BY`, `ORDER BY`, `ROWS BETWEEN`).
  * **Built-in Functions:** Almost all `pyspark.sql.functions` are available in SQL (e.g., `TRIM()`, `DATE_FORMAT()`, `CASE WHEN`).

-----

### V. Summary and Next Steps (5 min)

  * **Spark SQL** offers a powerful, optimized, declarative way to interact with structured data in Spark.
  * Use the **`%sql` magic command** in Databricks for querying.
  * **Temporary Views** (`createOrReplaceTempView`) are essential for passing DataFrames from the API into the SQL environment.
  * The **`spark.sql()`** command allows you to capture SQL query results back into a DataFrame for further programmatic processing.
  * **Next Lecture (L11):** We will begin Module 3 by diving into **Delta Lake**, the foundation of the Lakehouse architecture, and learn why it makes our data reliable.

  ## L11 - Introduction to Delta Lake


**Module:** 3: Modern Lakehouse Features

-----

### I. The Need for Data Reliability 
The traditional Data Lake (storing raw files like Parquet on cloud storage) introduced flexibility but lacked fundamental reliability features, leading to the "Data Swamp."

#### A. Data Lake Limitations

  * **Lack of Atomicity (Partial Writes):** If a job fails halfway through writing 1,000 files, users might see 500 incomplete files, corrupting the dataset.
  * **No Consistency (Dirty Reads):** One user could be reading data while another job is updating it, leading to inconsistent or incorrect query results.
  * **Schema Enforcement Issues:** New data with incompatible columns could be dumped into the dataset, breaking downstream ETL jobs.
  * **Inability to Mutate Data:** Updating or deleting specific rows (GDPR/CCPA compliance) was impossible without rewriting the entire dataset, which is slow and expensive.

#### B. Introducing Delta Lake

  * **Definition:** Delta Lake is an open-source storage layer that runs on top of your existing cloud storage (S3, ADLS, GCS). It brings **ACID properties** (Atomicity, Consistency, Isolation, Durability) to data lakes.
  * **Role in the Lakehouse:** It is the foundational component that transforms the raw file store into a reliable, transactional data platform.

-----

### II. The Core of Delta Lake: The Transaction Log 
Delta Lake achieves its reliability through a metadata file structure that sits alongside the data files.

#### A. Data Files vs. Log Files

  * **Data Files:** The actual Parquet files that store your data (e.g., `part-00000.parquet`).
  * **Transaction Log (or Delta Log):** A subdirectory named `_delta_log` containing a series of JSON and Parquet files. This log records **every transaction** (write, update, delete, merge) that has ever occurred on the Delta table.

#### B. How Transactions Work

1.  When a write operation starts, Spark performs the transformation on the cluster.
2.  New data is written to the table's directory (but is invisible).
3.  Upon successful completion, a new JSON file (a **Commit File**) is atomically written to the `_delta_log` directory.
4.  This commit file contains the instructions: "Remove file A, add new files B and C."
5.  Only after this file is successfully written is the new data considered part of the table.

#### C. Key Feature: ACID Properties

  * **Atomicity:** Ensures a change is either completed entirely or fails entirely—no partial visibility.
  * **Consistency:** Users see a consistent view of the data because readers only query the state defined by the latest successfully committed log file.
  * **Isolation:** Readers are isolated from writers; a query that starts before a job finishes will continue to read the *old* version of the data, guaranteeing repeatable reads.
  * **Durability:** Once a transaction is committed, the changes are permanent.

-----

### III. Basic Delta Table Operations 
You can interact with Delta tables using the same Spark API, simply by specifying the format.

#### A. Creating and Writing a Delta Table

When you write a DataFrame, specify the format as `"delta"`.

```python
# Create a DataFrame (as in previous lectures)
df_new = spark.createDataFrame([("Apple", 10), ("Banana", 20)], ["Item", "Count"])

# Write to a Delta table
df_new.write.format("delta").mode("overwrite").save("/mnt/delta/inventory")
```

#### B. Reading a Delta Table

Reading is the same as reading Parquet, but specifying the format `"delta"` unlocks transactional features.

```python
inventory_df = spark.read.format("delta").load("/mnt/delta/inventory")
inventory_df.show()
```

#### C. Schema Enforcement

  * Delta Lake automatically checks the schema of any incoming data against the existing table schema.
  * If the incoming schema is incompatible (e.g., trying to write a string to an integer column), the write operation will fail, preventing "Data Swamp" corruption.

-----

### IV. Summary and Next Steps (5 min)

  * **Delta Lake** provides the necessary **ACID properties** to turn a raw data lake into a reliable Lakehouse.
  * Its core is the **Transaction Log (`_delta_log`)**, which guarantees atomicity and consistency.
  * You interact with Delta tables by simply specifying `format("delta")` in your read and write operations.
  * Delta Lake enforces schemas to maintain data quality.
  * **Next Lecture (L12):** We will explore **Advanced Delta Lake Features**, focusing on time travel, data mutation (`MERGE INTO`), and table optimization.

  ## L12 - Advanced Delta Lake Features


**Module:** 3: Modern Lakehouse Features

-----

### I. Data Mutation: Updates, Deletes, and Merges 
The biggest advantage of Delta Lake over raw file formats is the ability to perform Data Manipulation Language (DML) operations—updating and deleting specific rows—without rewriting the entire dataset.

#### A. Updates and Deletes

These operations are executed using standard SQL or the DataFrame API, but they rely on the transaction log to work efficiently.

1.  **Deletion (`DELETE FROM`)**: Used for compliance (GDPR/CCPA) or removing bad data.
    ```python
    # Example: Delete all records for a specific user ID
    # Use SQL in a Databricks cell:
    # %sql
    # DELETE FROM delta.`/mnt/delta/inventory` WHERE user_id = 1234;
    ```
2.  **Updates (`UPDATE SET`)**: Used for correcting historical records or changing statuses.
    ```python
    # Example: Update status for a batch of orders
    # %sql
    # UPDATE delta.`/mnt/delta/inventory` SET status = 'Shipped' WHERE status = 'Pending';
    ```
      * **How it works:** Delta Lake finds the files containing the affected rows, copies those files, updates the rows in the copies, and then uses the transaction log to mark the old files for deletion and register the new files.

#### B. The `MERGE INTO` (Upsert) Command

The most powerful and frequently used Delta operation in ETL pipelines. It combines Insert, Update, and conditional Delete logic into a single transaction.

  * **Upsert:** A single statement that updates existing rows and inserts new rows from a source dataset into a target table.
  * **Syntax (SQL is most common):**
    ```sql
    -- Target is the Delta Table to modify, Source is the DataFrame with new data
    MERGE INTO target
    USING source
    ON target.id = source.id -- The key to match rows
    WHEN MATCHED THEN
        UPDATE SET target.col1 = source.col1
    WHEN NOT MATCHED THEN
        INSERT *;
    ```
  * **Use Case:** Implementing **Slowly Changing Dimensions (SCD Type 1)**, where you simply overwrite old data with the new data.

-----

### II. Time Travel (Data Versioning) 
The transaction log makes it possible to query previous versions of a Delta table, a feature known as **Time Travel** or **Delta Versioning**.

#### A. Why Use Time Travel?

1.  **Rollbacks:** Quickly revert a table to a previous state if a buggy ETL job runs.
2.  **Auditing and Reproducibility:** View the state of data at a specific point in time for regulatory compliance or debugging.
3.  **Data Quality Checks:** Run validation on the previous version of a table while the current job is running.

#### B. Querying Past Versions

You can query a specific version using either the version number or a timestamp.

1.  **Query by Version Number:**
    ```python
    # Read the table as it was after the Nth commit (Version 5)
    df_version = spark.read.format("delta").option("versionAsOf", 5).load(path)
    df_version.show()
    ```
2.  **Query by Timestamp:**
    ```python
    # Read the table as it existed exactly at 8:00 AM UTC
    df_time = spark.read.format("delta").option("timestampAsOf", "2025-09-29T08:00:00Z").load(path)
    df_time.show()
    ```

#### C. Full Rollback

The `RESTORE` command allows you to permanently revert the table to a previous version by creating a new commit in the transaction log.

-----

### III. Delta Table Optimization 
Over time, continuous updates and inserts can lead to numerous small files, which degrades Spark's performance. Optimization commands manage the physical layout of the data files.

#### A. The Small File Problem

Spark is optimized for processing large files. If a Delta table has millions of tiny files, Spark spends too much time opening, closing, and managing metadata for each file.

#### B. `OPTIMIZE` Command (File Compaction)

  * **Purpose:** Combines many small data files into fewer, larger, more efficient files.
    ```sql
    %sql
    OPTIMIZE delta.`/mnt/delta/inventory`;
    ```
  * **How it works:** It's a transaction that reads the small files, rewrites them into larger files (usually 1GB), and commits the new files to the log, marking the small ones for removal.

#### C. `ZORDER` Clustering

  * **Purpose:** Further improves query speed by physically co-locating related data in the same set of files. This technique works best for large tables.
  * **Use Case:** Greatly improves queries with filtering predicates (e.g., `WHERE country = 'USA' AND product = 'A'`).
    ```sql
    %sql
    OPTIMIZE delta.`/mnt/delta/inventory`
    ZORDER BY (country, product_id);
    ```
  * **Data Skipping:** When a query runs, the Z-Ordering metadata allows Spark to *skip* reading entire files that do not contain the required data range, leading to massive I/O savings.

#### D. `VACUUM` (File Cleanup)

  * **Purpose:** Permanently removes the old, physically deleted data files (the ones marked for removal by `OPTIMIZE`, `DELETE`, or `UPDATE`).
  * **Caution:** Requires a retention policy (default is 7 days) to ensure time travel queries can still function. **Never** run `VACUUM` with a zero retention period on a production table.

-----

### IV. Summary and Next Steps (5 min)

  * **DML operations** (`UPDATE`, `DELETE`, `MERGE INTO`) are possible thanks to the Delta transaction log. **`MERGE INTO`** is the standard for Upserts.
  * **Time Travel** allows querying data **`AS OF VERSION`** or **`TIMESTAMP`** for auditing and rollbacks.
  * **`OPTIMIZE`** (compaction) and **`ZORDER`** (clustering) are essential commands to maintain query performance over time.
  * **`VACUUM`** cleans up old files based on a safe retention policy.
  * **Next Lecture (L13):** We shift to **streaming ingestion** with **Auto Loader**, learning how to handle continuously arriving data efficiently.

  ## L13 - Data Ingestion with Auto Loader


**Module:** 3: Modern Lakehouse Features

-----

### I. The Challenge of Incremental Data Ingestion 
When data arrives continuously (e.g., streaming from IoT devices, log files), traditional batch processing falls short.

#### A. Limitations of Standard Batch Ingestion

  * **Polling:** Repeatedly listing the contents of a directory to find new files is slow, expensive (API calls to cloud storage), and inefficient for large numbers of files.
  * **Tracking:** Manually tracking which files have already been processed requires maintaining an external manifest, which is error-prone.
  * **Latency:** Long batch intervals increase the delay between data arrival and processing.

#### B. Introducing Auto Loader

  * **Definition:** Auto Loader is a Databricks feature that efficiently and incrementally processes new data files as they arrive in cloud storage (S3, ADLS, GCS).
  * **Key Benefit:** It automatically tracks which files have been processed, ensuring idempotency (files are processed once and only once) and efficiency.

-----

### II. Auto Loader Operation Modes 
Auto Loader can operate in two primary modes to discover new files, balancing efficiency and cost.

#### A. File Notification Mode (Recommended)

1.  **Mechanism:** Auto Loader sets up native cloud notification services (e.g., AWS SQS, Azure Event Grid) on the source cloud storage bucket/container.
2.  **How it Works:** When a new file is dropped, the cloud service sends a notification event to a queue, which Auto Loader monitors.
3.  **Benefit:** Highly scalable and cost-efficient because it avoids directory listing; it only processes files for which it receives an explicit notification.
4.  **Requirement:** Requires the user to configure the necessary cloud permissions and notification setup.

#### B. Directory Listing Mode (Simpler Setup)

1.  **Mechanism:** Auto Loader periodically lists the files in the input directory.
2.  **How it Works:** It maintains a **checkpoint location** to record metadata about the files it has seen and processed.
3.  **Benefit:** Requires no complex cloud configuration.
4.  **Drawback:** Can become slow and expensive when the input directory contains millions of files.

-----

### III. Implementing Auto Loader with Structured Streaming 
Auto Loader is integrated with the **Spark Structured Streaming API**, treating the incoming files as a continuous stream.

#### A. The `cloudFiles` Source

The configuration is passed to Spark using the special source format: `cloudFiles`.

```python
# 1. Define the input path and checkpoint location
input_path = "abfss://raw@datalake.dfs.core.windows.net/data/"
checkpoint_path = "/mnt/checkpoints/logs_stream/"

# 2. Configure Auto Loader options
auto_loader_options = {
    "cloudFiles.format": "json",      # Specify file format
    "cloudFiles.schemaLocation": checkpoint_path, # Location for schema and file tracking
    # Optional: File Notification setup, if applicable
    "cloudFiles.useNotifications": "true" 
}

# 3. Read the stream using Auto Loader
streaming_df = (
  spark.readStream
    .format("cloudFiles")
    .options(**auto_loader_options)
    .load(input_path)
)
```

#### B. The Checkpoint Location

  * This is mandatory and stores two critical pieces of information:
    1.  **File Tracking:** A log of all files processed to ensure idempotency.
    2.  **Schema Inference:** The inferred schema, which allows the stream to handle schema evolution (changes to the data structure) gracefully.

#### C. Handling Schema Evolution

  * If the incoming data changes its structure (e.g., a new column is added), Auto Loader needs instruction:
      * **`failOnNewColumns` (Default):** Stops the stream upon detecting a new column.
      * **`addNewColumns`:** Automatically adds new columns to the end of the DataFrame and continues processing.
      * **`rescue` (Recommended for Raw Data):** Writes data that couldn't be parsed to a special JSON column called `_rescued_data`, ensuring no data is lost while allowing the stream to continue.

-----

### IV. Writing the Streaming Sink (5 min)

Once the data is read and transformed, it needs to be written out continuously.

  * **Stream Sink (Output):** Typically a Delta Lake table, as it is transactional and handles concurrent reads and writes reliably.
  * **`writeStream` Configuration:**

<!-- end list -->

```python
# Write the stream to a Delta table
query = (
  streaming_df.writeStream
    .format("delta")
    .option("checkpointLocation", checkpoint_path) # Must specify a checkpoint again!
    .start("/mnt/delta/bronze_layer")
)
```

  * **Checkpoint Redundancy:** Note the checkpoint location is specified for **both** reading (tracking input files) and writing (tracking stream progress).

### V. Summary and Next Steps (5 min)

  * **Auto Loader** provides an efficient, incremental, and highly scalable solution for ingesting data landing in cloud storage.
  * It uses either **File Notification** (most efficient) or **Directory Listing** to find new files.
  * Auto Loader is implemented via the **`cloudFiles`** format within the **`readStream`** API.
  * The **Checkpoint Location** is mandatory for tracking progress and ensuring exactly-once processing.
  * **Next Lecture (L14):** We will deepen our understanding of **Structured Streaming** concepts, focusing on its architecture and how to perform stateful operations like aggregation.

  ## L14 - Introduction to Structured Streaming


**Module:** 3: Modern Lakehouse Features

***

### I. Streaming Fundamentals 
Structured Streaming is Spark's engine for processing continuous data streams. It allows you to express streaming computations in the same way you express batch computations.

#### A. The "Unbounded Table" Concept
* **Structured Streaming's Big Idea:** It treats a continuous data stream as a table that is continuously being appended to (**unbounded table**).
* **Benefit:** You use the exact same DataFrame API (e.g., `select()`, `filter()`, `join()`, `groupBy()`) for both batch and stream processing. Spark handles the complexity of incremental and distributed execution behind the scenes.
* **Micro-Batch Processing:** Structured Streaming processes data in small, continuous batches called **micro-batches**. This provides low latency (seconds) while leveraging Spark's high-throughput batch engine.

#### B. Streaming Sources and Sinks
* **Sources (Input):** Where the stream originates.
    * **Cloud Files (`cloudFiles`):** Covered in L13 (Auto Loader).
    * **Kafka/Event Hubs:** High-throughput message queues.
    * **Rate/Socket:** For simple testing and debugging.
* **Sinks (Output):** Where the results of the stream are written.
    * **Delta Lake:** The most common transactional sink.
    * **Console/Memory:** For testing and immediate visualization.
    * **Kafka/Event Hubs:** Writing results to another message queue.

---

### II. The Execution Model 
Understanding the flow of data and how state is maintained is crucial for building robust streaming applications.

#### A. The `readStream` and `writeStream`
1.  **Input Table:** Defined by `spark.readStream.format().load()`. New data is read into this logical table in each trigger interval.
2.  **Query:** Defined by the chained DataFrame transformations. Spark generates a new plan for the new data.
3.  **Result Table:** The output of the transformations.

#### B. The Checkpoint Location (Review and Deeper Dive)
* The **checkpoint location** is mandatory for all production streams.
* **Role:** Stores all the metadata needed to recover a stream's progress and state after a failure or intentional shutdown.
* **Contents:** Includes the schema, the progress of processed offsets/files, and any **state** that was computed (e.g., running counts).

#### C. Output Modes
Defines how the data in the Result Table is written to the Sink.

1.  **`Append` (Default):** Only new rows appended to the Result Table since the last trigger are written to the sink. (Suitable for simple ingestion/filtering).
2.  **`Complete`:** The entire updated Result Table is written to the sink every time. (Suitable for streams that use aggregation, where all aggregates need to be updated).
3.  **`Update`:** Only rows that have been updated since the last trigger are written to the sink. (Used for more optimized aggregation scenarios).

---

### III. Stateless vs. Stateful Operations 
Streaming operations are categorized by whether they need to remember information from previous micro-batches.

#### A. Stateless Operations (Easy)
* Operations that can be completed entirely based on the data in the **current micro-batch**.
* **Examples:** `select()`, `filter()`, `withColumn()`, simple projections.
* **Characteristic:** No internal "state" needs to be managed by the engine.

#### B. Stateful Operations (Challenging)
* Operations that require information from **previous micro-batches** to produce a correct result.
* **Examples:**
    * **Stream-Stream Joins:** Joining an incoming stream with an older part of the same stream or another stream.
    * **Aggregations:** Calculating a running count or sum (the stream must remember the count from the last batch).
* **State Management:** Spark automatically manages the state and stores it securely in the **checkpoint location** to ensure fault tolerance. Stateful operations often require defining **time windows** and **watermarks** (covered in L15).

---

### IV. Monitoring the Stream (5 min)

Once a stream is started, it runs indefinitely until manually stopped or until a failure.

* **The `StreamingQuery` Object:** The `writeStream.start()` action returns a `StreamingQuery` object.
* **Monitoring:** Use methods on this object to check status:
    * `query.isActive`: Checks if the stream is running.
    * `query.status`: Provides detailed information on processed batches and pending data.
    * `query.awaitTermination()`: Blocks the notebook until the query stops.

---

### V. Summary and Next Steps (5 min)

* **Structured Streaming** uses the familiar DataFrame API to process streams as continuously appending tables.
* Execution is based on **Micro-Batches**.
* The **Checkpoint Location** is vital for fault tolerance and state management.
* Differentiate between simple **Stateless** operations and complex **Stateful** operations (like aggregation).
* **Next Lecture (L15):** We will tackle the complexities of **Streaming Aggregation and Watermarking**, learning how to handle event time and late data arrival.

## L15 - Streaming Aggregation and Watermarking


**Module:** 3: Modern Lakehouse Features

-----

### I. The Challenge of Stateful Streaming Aggregation 
Aggregations like calculating a running total or a count per user are **Stateful Operations**—they require the stream to maintain a memory of past events.

#### A. Event Time vs. Processing Time

  * **Processing Time:** The time at which a data record is *processed* by the Spark cluster. This is easy to track but unreliable, especially in distributed systems where lag varies.
  * **Event Time (Crucial for Streaming):** The time at which the event *actually occurred*, usually embedded as a timestamp within the data record itself.
  * **The Problem:** Data streams are inherently messy. Events from the past may arrive late (out-of-order) due to network lag, device offline status, or batch loading.

#### B. The Need for Time Windows

To perform aggregations (e.g., "count events every 5 minutes"), we cannot use a simple `groupBy()`. We must define a **Time Window** based on the event time.

-----

### II. Time Window Aggregation 
Time windows segment the data into fixed, non-overlapping intervals based on the event time column.

#### A. The `window()` Function

The `window()` function creates a new column defining the boundaries (start and end timestamps) of the aggregation interval.

```python
from pyspark.sql.functions import window, col, count

# 1. Define the window duration (e.g., 10 minutes)
windowed_df = streaming_df.groupBy(
    window(col("event_timestamp"), "10 minutes"), # Group by 10-minute intervals
    col("device_id") # Additional partitioning key
).agg(
    count(col("event_timestamp")).alias("event_count")
)
```

#### B. Tumbling vs. Sliding Windows

  * **Tumbling Window (Used Above):** Non-overlapping, fixed-size windows (e.g., 12:00-12:10, 12:10-12:20). Every event belongs to exactly one window.
  * **Sliding Window:** Overlapping windows (e.g., a 10-minute window that slides every 5 minutes). Used for calculations like moving averages.

#### C. Output Mode for Aggregation

When using `groupBy()` and `agg()`, you must use the **`Update`** or **`Complete`** output mode in your `writeStream`:

  * **`Complete`:** Writes the full, current result set (all window totals) every trigger.
  * **`Update` (More Efficient):** Writes only the window totals that have been updated by the latest micro-batch.

-----

### III. Watermarking: Handling Late Data 
Since data arrives out-of-order, a stream's state could grow infinitely if it waits forever for late records. **Watermarking** tells Spark when it can safely discard old state.

#### A. Defining the Watermark

The watermark is a time threshold that specifies how late an event can be and still be considered for an aggregation window.

  * **Syntax:** `df.withWatermark(eventTimeColumn, delayThreshold)`
  * **Example:** `.withWatermark("event_timestamp", "1 minute")` means Spark will wait up to 1 minute past the latest seen event time before closing a window.

#### B. How Watermarking Works

1.  Spark tracks the **maximum event time** seen so far across all partitions.
2.  The **Watermark Time** is calculated as: `(Maximum Event Time) - (Delay Threshold)`.
3.  Any event arriving with an event time **less than** the Watermark Time is considered **too late** and is dropped.
4.  Once the watermark surpasses the end of a time window, that window is finalized, and its state is evicted (removed from memory and checkpoint).

#### C. Importance of the Order

The `withWatermark()` operation **must** be called before the stateful operation (like `groupBy()` and `window()`).

```python
# The fully configured streaming aggregation
final_df = (
  streaming_df
    .withWatermark("event_timestamp", "3 minutes") # 1. Define max lateness
    .groupBy(
        window(col("event_timestamp"), "5 minutes"), # 2. Define the aggregation window
        col("device_id")
    ).agg(...)
)
```

-----

### IV. Stream-Stream Joins and State Management (5 min)

Stateful concepts extend to joins, where Spark needs to hold one stream's data in memory while waiting for the matching record from the second stream.

  * **Stream-Stream Joins:** Joining two continuously flowing streams is extremely challenging and requires both:
    1.  A **Watermark** defined on both streams.
    2.  An **Event Time Constraint** in the join condition to limit the time range in which records from the two streams can be matched.
  * **Example Constraint:** `(left.timestamp >= right.timestamp - interval 1 hour) AND (left.timestamp <= right.timestamp + interval 1 hour)`

-----

### V. Summary and Next Steps (5 min)

  * **Streaming Aggregation** requires defining a **Time Window** based on the event time.
  * **Watermarking** (`withWatermark()`) is the mechanism that manages state by defining an acceptable delay threshold for late data.
  * Data older than the watermark is dropped, allowing Spark to safely **evict old state** and prevent infinite memory growth.
  * When aggregating, use the **`Update`** or **`Complete`** output mode.
  * **Next Lecture (L16):** We will transition to performance and optimization with **Performance Tuning Fundamentals**, focusing on identifying and solving common Spark bottlenecks.

  ## L16 - Performance Tuning Fundamentals


**Module:** 4: Optimization, Governance, and Deployment

***

### I. The Spark Performance Equation 
Performance in Spark is about minimizing the time spent on three major activities: reading/writing data, network I/O, and CPU computation. Tuning focuses on reducing bottlenecks in this process.

#### A. Identifying Bottlenecks
The primary tool for diagnosing performance issues is the **Spark UI**.

* **Spark UI in Databricks:** Accessible via the cluster detail page, the Spark UI provides granular details about every job, stage, and task executed on the cluster.
* **Key Areas to Monitor:**
    1.  **Stages:** Look for long-running stages, especially those with many tasks.
    2.  **Summary Metrics:** Check for high values in **Shuffle Write/Read** (network cost) and **Spill** (disk I/O).
    3.  **Event Timeline:** Look for uneven distribution of work or large time gaps between stages.

#### B. The Core Cost: Shuffle Operations
* A **Shuffle** is the process of redistributing data across the cluster for wide transformations (joins, aggregations, repartitioning).
* **Cost:** Shuffles are extremely expensive because they involve serialization, network transfer, and deserialization, causing data to be written to disk multiple times. **Minimize Shuffles whenever possible.**

---

### II. Common Performance Bottlenecks 
These issues are typically visible as long-running, inefficient stages in the Spark UI.

#### A. Data Skew
* **Problem:** Data is unevenly distributed based on the partitioning or join key (e.g., one key represents 80% of the rows).
* **Result:** The worker node processing the skewed key becomes a **bottleneck** because it receives a disproportionate amount of data, leading to a long tail of slow tasks while other workers are idle.
* **Mitigation (Basic):** **Filter out skewed keys** if they are not critical, or consider more advanced techniques like **salting** (adding a random prefix to the key) to manually distribute the skewed data.

#### B. Too Many Small Files (File Explosion)
* **Problem:** Spark is optimized for processing files in the 100MB to 1GB range. Repeated `append` operations can create millions of tiny files (kilobytes in size).
* **Result:** Spark spends excessive time listing, opening, and closing file handles, which wastes I/O and metastore resources.
* **Mitigation:** Use the **`OPTIMIZE`** command (covered in L17) to compact small files into larger ones.

#### C. Data Spill
* **Problem:** A worker node runs out of available memory while performing a stage (e.g., during a large shuffle or aggregation).
* **Result:** The worker is forced to write intermediate data from memory to local disk storage, an operation known as **Spilling**. Disk I/O is much slower than in-memory processing.
* **Mitigation:**
    1.  Increase the cluster memory (use memory-optimized worker types).
    2.  Increase the number of partitions to distribute the load among more workers.

---

### III. Execution Optimization Techniques 
These techniques should be applied programmatically to improve how data is handled across the cluster.

#### A. Broadcast Hash Join (Review)
* **Principle:** When joining a large DataFrame with a small DataFrame, explicitly using the **`broadcast()`** function eliminates the shuffle for the large DataFrame.
* **Benefit:** The small DataFrame is copied to all worker nodes, allowing the large DataFrame's partitions to be joined locally. This is typically the single biggest performance gain for star-schema joins.

#### B. Repartition vs. Coalesce
These are both transformations that change the number of partitions, but they have different costs.

| Command | Purpose | Network Cost | Use Case |
| :--- | :--- | :--- | :--- |
| **`repartition(N)`** | Changes the number of partitions to *N*. | **High (Full Shuffle)** | When increasing partitions or eliminating skew. |
| **`coalesce(N)`** | Reduces the number of partitions to *N*. | **Low (Avoids Full Shuffle)** | Only when reducing partitions. Can cause data skew if N is too small. |

* **Rule:** Use `coalesce()` only to reduce partitions *before writing* (to prevent small files). Use `repartition()` when you need to increase parallelism or fix existing skew.

#### C. Caching/Persisting
* **Principle:** Saves an intermediate DataFrame to memory (or disk) so it doesn't need to be recomputed for subsequent actions.
* **Syntax:** `df.cache()` or `df.persist(storage_level)`.
* **Use Case:** When a DataFrame is accessed multiple times by different operations (e.g., training multiple ML models on the same feature set). **Always** remember to `df.unpersist()` when you are done to free up cluster memory.

---

### IV. Summary and Next Steps (5 min)

* Performance tuning starts with analyzing the **Spark UI** to identify bottlenecks, particularly **Shuffles** and **Spills**.
* Mitigate the **Small File Problem** and address **Data Skew** proactively.
* The **Broadcast Hash Join** is the most valuable performance optimization to apply in joins.
* Use `repartition()` carefully (it shuffles), and use `coalesce()` to reduce partitions efficiently before writing.
* **Next Lecture (L17):** We will focus on physical optimization of the data itself using **Delta Table Optimization** features like `OPTIMIZE` and `ZORDER`.

## L17 - Delta Table Optimization


**Module:** 4: Optimization, Governance, and Deployment

-----

### I. The Need for Physical Optimization 
While Spark tuning (L16) optimizes the execution *engine*, Delta optimization focuses on the physical *layout* of the data files themselves, leading to massive I/O gains.

#### A. Data Skipping

  * **Principle:** When data is organized physically, the Spark engine can use metadata to determine which data files are **irrelevant** to a query's filter clause.
  * **Benefit:** By skipping entire files, the time spent reading from cloud storage is dramatically reduced. This is particularly effective with columnar formats (like Delta/Parquet) because the file contains summary statistics (min/max values) for each column.

#### B. The Small File Problem (Review)

  * As covered in L16, too many small files kill performance. Delta Lake provides tools to solve this problem permanently.

-----

### II. File Compaction with `OPTIMIZE` 
The primary tool for managing the physical file size of a Delta table is the `OPTIMIZE` command.

#### A. The `OPTIMIZE` Command

  * **Purpose:** Reads all small files within a table or partition and rewrites them into larger, optimized files (typically aiming for 1GB each).
  * **Execution:** It runs as a Spark job, ensuring the process is distributed and efficient.
    ```sql
    -- SQL Syntax in Databricks
    %sql
    OPTIMIZE delta.`/mnt/delta/inventory`;

    -- Optimize only a specific partition (more targeted)
    OPTIMIZE delta.`/mnt/delta/inventory` WHERE date = '2025-09-01';
    ```
  * **Transactionality:** The `OPTIMIZE` operation is a transaction. It adds the new, compacted files to the log and logically removes the old, small files, maintaining ACID guarantees.

#### B. Auto Compaction

  * Databricks can be configured for automatic, background compaction, which helps continuously maintain file sizes after writes and updates without manual intervention. This is usually enabled at the cluster or table level.

-----

### III. Data Organization with `ZORDER` 
The `ZORDER` command is the key to maximizing Data Skipping performance on your largest tables.

#### A. Z-Ordering Concept

  * **Problem with Single-Column Sorting:** If you sort your data by `Country`, queries filtering by `Product` will still have to read files spanning all products.
  * **Solution:** Z-Ordering is a multi-dimensional clustering technique. It organizes related values across **multiple columns** (e.g., `Country` AND `Product`) physically near each other on disk.
  * **Benefit:** Queries that filter on any combination of the Z-Ordered columns can skip much more data.

#### B. `ZORDER` Implementation

  * **Syntax:** `ZORDER` is run as part of the `OPTIMIZE` command.

    ```sql
    %sql
    OPTIMIZE delta.`/mnt/delta/sales_transactions`
    ZORDER BY (customer_id, transaction_date);
    ```

  * **Choosing Columns:**

      * **Select up to 3-5 columns.** Adding too many columns is counter-productive.
      * Choose columns used frequently in `WHERE` clauses (filters) and join conditions.
      * Do not Z-Order on extremely high-cardinality columns (like UUIDs) or extremely low-cardinality columns (like a boolean flag).

#### C. Continuous Z-Ordering

For tables that are continuously receiving new data, you must run the `OPTIMIZE ... ZORDER` command periodically (e.g., daily) to maintain the optimal clustering on the newly arrived files.

-----

### IV. Other Optimization Techniques (5 min)

#### A. Delta Caching (Cluster Configuration)

  * When using Databricks, the cluster can be configured with a caching layer (separate from Spark's native cache).
  * **Role:** Caches the actual data files (Parquet blocks) on the local SSDs of the worker nodes.
  * **Benefit:** Greatly accelerates queries that repeatedly access the same set of files by eliminating repeated reads from slow cloud storage.

#### B. Liquid Clustering (Newer Feature)

  * **Concept:** A next-generation table organization technique (replacing partitioning and Z-Ordering) that automatically adapts the data layout based on query patterns.
  * **Benefit:** Simplifies data architecture by eliminating the need to choose partition keys upfront.

-----

### V. Summary and Next Steps (5 min)

  * **Physical Optimization** is achieved by organizing data to enable **Data Skipping**.
  * **`OPTIMIZE`** is used to solve the **Small File Problem** by compacting files.
  * **`ZORDER BY`** clusters related data across multiple dimensions to maximize filter performance on large tables.
  * **Next Lecture (L18):** We will conclude the data management focus by exploring **Databricks SQL and Data Warehousing**, including the essential topic of **Unity Catalog** for governance.

  ## L18 - Databricks SQL and Data Governance


**Module:** 4: Optimization, Governance, and Deployment

***

### I. The Databricks SQL Interface 
The Databricks SQL (DBSQL) interface provides a dedicated, highly optimized environment for analysts and BI users, separating the analytics workload from the engineering workload.

#### A. Databricks SQL Endpoints (Warehouses)
* **Purpose:** A dedicated, scalable compute resource designed specifically for running low-latency SQL queries.
* **Separation of Compute:** They are distinct from the All-Purpose clusters used by data engineers. This prevents large, exploratory BI queries from impacting mission-critical ETL jobs.
* **Optimization:** SQL Endpoints automatically handle complex resource management and leverage native cloud technologies (like Photon, Databricks' optimized vectorization engine) for faster SQL query execution.

#### B. The DBSQL Workspace
* **SQL Editor:** A streamlined interface for writing and executing pure SQL queries.
* **Queries and Dashboards:** Users can save queries, define visualizations, and organize them into collaborative dashboards. This enables self-service BI directly on the Lakehouse data.
* **Alerts:** Set up automated email notifications when query results meet certain business thresholds (e.g., sales drop below a defined minimum).

---

### II. Introduction to Unity Catalog 
Data Governance is the framework that ensures data is secure, reliable, and accessible only to authorized users. Unity Catalog is Databricks' unified governance layer for the Lakehouse.

#### A. The Problem Unity Catalog Solves
* **Fragmentation:** Historically, governance (security, audit logs) was managed separately for the Data Lake (cloud storage) and the Data Warehouse (Spark/Databricks).
* **The Solution:** Unity Catalog (UC) provides a single, centralized layer for governance across all data and AI assets (tables, files, models) in your Lakehouse, regardless of where the data resides or which language (Python, SQL) is used.

#### B. The Three-Level Namespace
UC organizes data using a hierarchical, familiar structure, similar to traditional databases:

$$\text{Catalog} \rightarrow \text{Schema (Database)} \rightarrow \text{Table/View}$$

* **Catalog:** The highest level, often mapping to a data environment (e.g., `prod`, `dev`) or business unit.
* **Schema (Database):** A logical grouping of tables (e.g., `sales_data`, `hr_data`).
* **Table/View:** The actual data assets.

#### C. Centralized Security and Access Control
* **Principle:** Security is defined once in Unity Catalog and applied everywhere.
* **Granularity:** You can grant permissions at the catalog, schema, table, or even **column and row level**.
    * **Example (Row-Level Security):** Grant a regional manager access to only the rows where `region = 'North'`.
    * **Example (Column Masking):** Allow all users to see the `customer` table but mask the `SSN` column for standard users.
* **Audit Logs:** UC records detailed audit logs of all data access and usage, essential for compliance.

---

### III. Data Organization: The Medallion Architecture 
The Medallion Architecture is a best practice for structuring data within the Lakehouse, organizing data quality and complexity into three distinct tiers or "layers."

#### A. Bronze Layer (Raw Data)
* **Goal:** Ingestion and History.
* **Content:** Raw, source data, written directly to the Delta Lake.
* **Characteristics:** Data is kept in its original format with full fidelity. Minimal cleaning or schema enforcement. Time travel is crucial here.

#### B. Silver Layer (Cleaned, Integrated Data)
* **Goal:** Cleansing and Conforming.
* **Content:** Cleaned, filtered, and integrated data.
* **Transformations:** Basic cleaning (handling nulls, casting data types), deduplication, validation, and complex joins (e.g., joining sales with product codes). This is the source for further transformations.

#### C. Gold Layer (Curated, Aggregated Data)
* **Goal:** Business Reporting and BI.
* **Content:** Highly refined, aggregated, and business-ready data.
* **Structure:** Often stored in a dimensional model (star or snowflake schema) optimized for quick BI tool consumption via Databricks SQL Endpoints. This layer typically contains aggregate tables (e.g., daily sales totals, monthly active users).

---

### IV. Summary and Next Steps (5 min)

* **Databricks SQL Endpoints** provide dedicated, optimized compute for analyst and BI workloads.
* **Unity Catalog** is the centralized **governance layer**, enabling fine-grained security (column/row level) and a unified view of data assets.
* The **Medallion Architecture (Bronze $\rightarrow$ Silver $\rightarrow$ Gold)** is the standard practice for structuring and improving data quality across the Lakehouse.
* **Next Lecture (L19):** We will cover **Designing and Scheduling Data Pipelines** using Databricks Workflows and introduce the concept of Delta Live Tables (DLT).

## L19 - Designing and Scheduling Data Pipelines


**Module:** 4: Optimization, Governance, and Deployment

-----

### I. Data Pipeline Design: The Medallion Architecture in Practice 
The Medallion Architecture (Bronze, Silver, Gold, introduced in L18) provides the blueprint for building reliable, multi-stage data pipelines.

#### A. Bronze Layer Pipeline

  * **Input:** Raw files from cloud storage (e.g., S3, ADLS).
  * **Processing:** Primarily uses **Auto Loader** (L13) with **Structured Streaming** (L14).
  * **Goal:** Ingest data quickly with minimal transformation. Use the **`_rescued_data`** column for error handling to avoid dropping unparseable records.
  * **Output:** Delta tables in the Bronze schema.

#### B. Silver Layer Pipeline

  * **Input:** Bronze Delta tables.
  * **Processing:** Can use **Batch** or **Streaming**. Often involves complex **PySpark/SQL transformations** (L7, L10), **joins** (L8), and **deduplication**.
  * **Goal:** Cleanse, standardize, and conform data to standard business keys.
  * **Output:** Delta tables in the Silver schema.

#### C. Gold Layer Pipeline

  * **Input:** Silver Delta tables.
  * **Processing:** Typically **Batch** or scheduled **Streaming**. Focuses on **aggregation** (L7) and **window functions** (L9).
  * **Goal:** Create summarized, denormalized tables optimized for BI tools and low-latency querying via Databricks SQL Endpoints (L18).
  * **Output:** Highly curated Delta tables in the Gold schema.

-----

### II. Production Orchestration with Databricks Workflows 
Once the code for each pipeline stage is written, Databricks **Workflows** (formerly called Jobs) is the native tool for scheduling, managing, and monitoring production execution.

#### A. Jobs (Workflows) Configuration

1.  **Tasks:** A job is composed of one or more **tasks**. Each task can be a notebook, a Python script, a SQL file, or a Delta Live Tables pipeline.
2.  **Job Cluster:** Jobs should always use a **Job Cluster** (L2). This cluster is created just for the job and terminates immediately after, minimizing idle compute costs.
3.  **Scheduling:** Define the trigger (e.g., daily at 3 AM, every 5 minutes, or triggered by a cloud event).

#### B. Defining Dependencies

  * Tasks are linked by dependencies, ensuring stages run in the correct order.
  * **Example:** The Silver processing task **must** wait for the Bronze ingestion task to succeed before it starts. This creates a robust **DAG (Directed Acyclic Graph)** for the entire pipeline.

#### C. Monitoring and Alerting

  * **Execution History:** Databricks tracks the run history, duration, and associated cluster logs for every job run.
  * **Alerts:** Configure alerts to notify engineers (e.g., via email, Slack) immediately when a job fails or if its runtime exceeds a defined threshold.

-----

### III. Introduction to Delta Live Tables (DLT) 
Delta Live Tables is a framework built on Databricks that simplifies the development and deployment of ETL pipelines by using a **declarative approach**.

#### A. Declarative ETL

  * **The Problem DLT Solves:** Traditional ETL requires developers to manually define *how* to execute data dependencies, handle retries, manage state, and deal with schema evolution.
  * **DLT Solution:** Developers only declare *what* the final tables and views should look like and *which data quality constraints* they should obey. DLT automatically handles the "how."

#### B. Key DLT Features

1.  **Automatic Dependency Management:** DLT automatically builds the full pipeline DAG based on the declared table dependencies.
2.  **Data Quality Enforcement:** Define **expectations** (assertions) on data quality (e.g., "column A must not be NULL"). DLT monitors these, quarantines bad records, or fails the pipeline based on the severity.
      * **Quarantine:** Bad records can be automatically routed to a dedicated "quarantine" table for later review, preventing pipeline failure.
3.  **Automatic Schema Handling:** DLT automatically manages schema evolution based on configuration (e.g., "append new columns and fail if a column type changes").
4.  **Optimized Execution:** DLT automatically optimizes the underlying Spark processing, compaction, and clustering.

#### C. DLT Syntax Example (Conceptual)

Instead of writing a stream job, you write simple table definitions:

```python
# Instead of complex spark.readStream...
@dlt.table(name="silver_customers")
def silver_customers():
  # DLT automatically manages incremental processing from the bronze table
  return dlt.read("bronze_raw").filter(col("customer_id").isNotNull())

@dlt.table(name="gold_summary")
def gold_summary():
  # DLT manages the dependency on silver_customers
  return dlt.read("silver_customers").groupBy("city").agg(F.sum("revenue"))
```

-----

### IV. Summary and Next Steps (5 min)

  * Data pipelines are designed using the **Medallion Architecture** (Bronze $\rightarrow$ Silver $\rightarrow$ Gold) to progressively increase data quality.
  * **Databricks Workflows** are the native scheduling and orchestration tool, managing dependencies via a DAG and using cost-effective Job Clusters.
  * **Delta Live Tables (DLT)** offers a powerful, **declarative** alternative for building robust pipelines, simplifying schema management and data quality enforcement.
  * **Next Lecture (L20):** We will conclude with a **Final Project and Best Practices**, reviewing all core concepts and discussing code standards.

  ## L20 - Final Project and Best Practices


**Module:** 4: Optimization, Governance, and Deployment

-----

### I. End-to-End Project Review and Synthesis 
This final section synthesizes all concepts into a single, comprehensive data pipeline, reviewing the core concepts learned throughout the course.

#### A. The End-to-End Pipeline Goal

Build a pipeline that continuously ingests raw web log data, cleanses it, calculates key business metrics, and serves the results for BI reporting.

| Pipeline Stage | Concepts Used | Technologies/Commands |
| :--- | :--- | :--- |
| **Ingestion (Bronze)** | Structured Streaming, Incremental Loading, File Format | **Auto Loader** (`cloudFiles`), `readStream`, `format("delta")` |
| **Cleansing (Silver)** | Transformations, Joins, Data Quality | `withColumn()`, **`MERGE INTO`** (for upserting customer info), **UDFs** (sparingly), `filter()`, `printSchema()` |
| **Analytics (Gold)** | Stateful Aggregation, Optimization | **Window Functions** (e.g., running total), **`groupBy()`** & **`agg()`**, **`OPTIMIZE ZORDER`** |
| **Serving & Orchestration** | Governance, Compute, Automation | **Databricks Workflows** (scheduling), **Job Cluster**, **Unity Catalog** (security), **Databricks SQL Endpoint** |

#### B. Key Takeaways Review

  * **Architecture:** The **Lakehouse** is the unified data platform, built on **Delta Lake** for ACID properties.
  * **Compute:** **Spark** is the distributed engine. Performance is dictated by minimizing **Shuffles** and maximizing **Broadcast Joins**.
  * **Reliability:** The **Transaction Log** and **Checkpoints** are the foundations of fault-tolerant processing (both batch and streaming).

-----

### II. Production Code Best Practices 
Moving from exploratory notebook code to maintainable, production-ready ETL requires adopting standard software engineering practices.

#### A. Modularity and Reusability

  * **Avoid Monolithic Notebooks:** Do not put the entire Bronze-to-Gold logic in a single file. Break code into specialized functions and separate notebooks (one for Bronze, one for Silver, etc.).
  * **Function Wrapping:** Wrap all core logic into reusable functions with clear inputs (DataFrames, configuration) and outputs (DataFrames).
  * **Using `%run`:** Use the `%run /path/to/notebook` magic command to import functions and setup code from helper notebooks.

#### B. Configuration Management

  * **Separation of Concerns:** Hard-code file paths, credentials, and configuration parameters should be moved out of the main logic notebooks.
  * **Databricks Secrets:** Use the **Databricks Secrets Utility** (integrated with Unity Catalog) to securely store and reference credentials (API keys, service principals). **Never** paste passwords or keys into a notebook.

#### C. Error Handling

  * **PySpark:** Utilize standard Python **`try...except...finally`** blocks to gracefully handle potential runtime errors (e.g., file not found, network timeout).
  * **Logging:** Use Python's built-in **`logging`** library instead of just `print()` statements. Structured logging helps diagnose issues during production runs.

-----

### III. Final Project: Practical Guide 
**Goal:** Create a Gold table summarizing daily active users (DAU) and their highest activity level.

1.  **Read Bronze:** Use `spark.read.format("delta").load("/bronze/logs")`.

2.  **Cleanse/Transform (Silver):** Filter out bot traffic (`.filter(col("user_agent") != 'bot')`). Create a temporary view: `cleaned_df.createOrReplaceTempView("v_cleaned_logs")`.

3.  **Aggregate (Gold - SQL):** Use Spark SQL for aggregation:

    ```sql
    %sql
    CREATE OR REPLACE TABLE gold_dau AS
    SELECT 
      DATE(timestamp) AS activity_date,
      user_id,
      MAX(activity_level) AS max_level
    FROM v_cleaned_logs
    GROUP BY 1, 2;
    ```

4.  **Optimize:** Schedule an optimization job: `OPTIMIZE gold_dau ZORDER BY (activity_date, user_id)`.

5.  **Deployment:** Configure a **Databricks Workflow** to run the clean/aggregate notebooks daily on a Job Cluster.

-----


