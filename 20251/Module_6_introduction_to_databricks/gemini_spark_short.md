# **Big Data Processing in Spark using Databricks: Consolidated Notes (L1-L20)**

This document synthesizes all 20 lectures, covering the fundamental architecture of Spark, core data manipulation, the Lakehouse platform (Delta Lake), optimization, and production deployment.

## **1\. Introduction to Big Data and Spark**

### **I. The Challenge of Big Data**

Big Data is characterized by the **Three Vs**:

* **Volume:** The sheer amount of data generated.  
* **Velocity:** The speed at which data is generated and must be processed (streaming).  
* **Variety:** The diversity of data types (structured, semi-structured, unstructured).

### **II. Why Apache Spark?**

Spark is a unified analytics engine for large-scale data processing.

* **Speed:** Achieves high performance through in-memory computation and optimized execution.  
* **General Purpose:** Supports multiple languages (Python, Scala, R, SQL).  
* **Unification:** Combines batch processing, streaming, SQL, and machine learning into a single API.

## **2\. Spark Architecture Fundamentals**

### **I. Cluster Components**

Spark operates on a cluster of machines.

1. **Driver Program:**  
   * Runs the main() function and creates the **SparkContext**.  
   * Creates the **DAG (Directed Acyclic Graph)** of operations.  
   * Schedules tasks to be run on the executors.  
2. **Cluster Manager:** Acquires resources on the cluster (e.g., YARN, Kubernetes, Databricks).  
3. **Executors (Workers):**  
   * Processes tasks and stores data partitions in memory.  
   * Reports results and status back to the Driver.

### **II. RDDs and the DAG**

* **Resilient Distributed Datasets (RDDs):** The foundational abstraction in Spark. A fault-tolerant, immutable, distributed collection of objects. **DataFrames abstract away RDDs.**  
* **DAG:** The logical execution plan created by the Driver. It's built up lazily by transformations and executed only when an action is called.

## **3\. Introduction to Databricks**

### **I. The Lakehouse Platform**

Databricks integrates the flexibility and scale of a Data Lake (cheap storage) with the reliability and structure of a Data Warehouse (ACID properties).

### **II. Cluster Management**

* **All-Purpose Clusters:** Used for interactive development, exploratory analysis, and running ad-hoc commands (often left running).  
* **Job Clusters:** Automatically created to run a specific job (workflow) and terminated immediately upon completion. **Highly recommended for cost efficiency in production.**

### **III. Databricks Notebooks**

* **Interoperability:** Seamlessly switch between languages within a single notebook cell using **Magic Commands** (e.g., %sql, %python, %scala).  
* **Auto-scaling:** Clusters can automatically add or remove worker nodes based on workload demands.

## **4\. DataFrames: The Core Abstraction**

### **I. Definition**

A **DataFrame** is a distributed collection of data organized into named columns, analogous to a table in a relational database.

* **Structure:** Composed of **Schema** (column names and data types) and **Data** (the distributed rows).  
* **Advantage over RDDs:** Provides schema information, allowing the Catalyst Optimizer (L10) to generate highly efficient execution plans.

### **II. Lazy Evaluation Principle**

Spark never executes a transformation immediately. It records the transformation in the DAG until an **Action** is called, which triggers the actual distributed computation across the cluster (L5).

## **5\. Working with Data: Transformations and Actions**

The execution model in Spark is based on **lazy evaluation**, differentiating operations into two types.

### **I. The Core Dichotomy: Transformations vs. Actions**

| Feature | Transformation | Action |
| :---- | :---- | :---- |
| **Definition** | Operations that produce a **new DataFrame**. | Operations that trigger the execution of the DAG. |
| **Execution** | **Lazy** (builds the plan \- DAG) | **Eager** (initiates work on the cluster) |
| **Output** | New DataFrame pointer | Local Value (count, array) or External Write |
| **Examples** | select(), filter(), withColumn(), groupBy() | show(), count(), collect(), write(), toPandas() |

### **II. Essential Transformations**

Transformations are categorized as Narrow or Wide:

* **Narrow Transformations** (no shuffle required): select(), filter(), withColumn(), drop(), withColumnRenamed(), cast().  
* **Wide Transformations** (shuffle required): groupBy(), join(), repartition(), orderBy().

### **III. Essential Actions**

* **show(n):** Displays the first n rows. Most common for development.  
* **count():** Returns the total number of rows.  
* **collect():** **CAUTION:** Returns all data to the Driver program. Use only on very small datasets to prevent Driver OutOfMemory errors.  
* **write:** Persists the result to a storage system (e.g., Delta Lake, Parquet).

## **6\. Data Ingestion and Sources**

Data must be read from distributed storage into a Spark DataFrame using the spark.read interface.

### **I. Spark's Read Interface**

The pattern is: spark.read.option("key", "value").format("format").load("path").

### **II. Working with File Formats**

| Format | Type | Description | Best Practice |
| :---- | :---- | :---- | :---- |
| **CSV/JSON** | Row-Oriented | Human-readable, flexible, poor query performance. | Read raw, transform to columnar immediately. |
| **Parquet** | **Columnar** | Analytics standard. Stores data column-by-column, enabling **Columnar Pruning**. | Preferred format for storing large tables. |
| **Delta Lake** | Columnar \+ Log | Parquet files plus a transaction log, adding ACID properties. | Preferred format in the Lakehouse. |

**Schema Management:** Always prefer using a predefined schema (.schema(my\_schema)) over using .option("inferSchema", "true"). Inference requires an extra data pass and is slow.

### **III. Accessing Data in Databricks**

Data is typically accessed via:

1. **DBFS Paths (dbfs:/):** An abstraction over mounted cloud storage.  
2. **Direct Cloud Paths:** Using standard cloud prefixes (e.g., s3://, abfss://), relying on secure cluster configurations (IAM roles/Service Principals).

## **7\. Advanced Data Manipulation**

Complex data cleaning and business logic require the Spark SQL Functions library.

### **I. Spark SQL Functions Library (F)**

Imported as from pyspark.sql import functions as F.

* **String Functions:** F.upper(), F.trim(), F.concat().  
* **Date/Time Functions:** F.date\_format(), F.year(), F.to\_timestamp().  
* **Mathematical/Array:** F.round(), F.size(), F.explode().

### **II. Conditional Logic**

* **when().otherwise():** Spark's equivalent of the SQL CASE statement.  
  df \= df.withColumn(  
      "Group",  
      F.when(col("score") \> 90, F.lit("A")).otherwise(F.lit("B"))  
  )

* **F.lit():** Used to introduce a literal (constant) value into a DataFrame expression.

### **III. Grouping and Aggregation (Wide Transformation)**

* **groupBy() and agg():** Used to summarize data, triggering a shuffle.  
* **Advanced Aggregation:**  
  * **rollup():** Creates subtotals for multiple grouping columns in a hierarchy (e.g., total sales per year, per month, and grand total).  
  * **cube():** Creates subtotals for all possible combinations of grouping columns.

### **IV. User-Defined Functions (UDFs)**

* **Definition:** Allows writing custom processing logic in Python/Scala.  
* **Performance Warning:** Python UDFs require data serialization between the JVM (Spark) and the Python interpreter, leading to significant overhead. **Avoid UDFs** if a built-in Spark function can achieve the same result.

## **8\. Joins and Set Operations**

Combining datasets is a Wide Transformation, demanding optimization.

### **I. Joins in Spark (Wide Transformation)**

The syntax is df\_left.join(df\_right, on="key\_column", how="join\_type").

| Join Type (how) | Description | Use Case |
| :---- | :---- | :---- |
| **inner** | Returns only matching keys in both DFs. | Finding common records. |
| **left\_outer** | All left rows, matching right columns (null otherwise). | Preserving primary dataset. |
| **left\_semi** | Returns only left rows whose key exists in the right. **Fastest filter.** | Checking existence efficiently. |
| **left\_anti** | Returns only left rows whose key **does not** exist in the right. | Finding unmatched/orphaned records. |
| **cross** (Cartesian) | Returns the Cartesian product (M \* N rows). **DANGEROUS** on large datasets. | Complex statistical modeling; must be explicit. |

### **II. Join Optimization: Broadcast Hash Join (BHJ)**

* **Principle:** When joining a large DataFrame with a small DataFrame (typically up to a few hundred MB), use the broadcast() function.  
* **Benefit:** The small DataFrame is copied to all worker nodes, **eliminating the shuffle** for the large DataFrame, which is the single biggest performance gain for star-schema joins.

### **III. Set Operations**

Require the DataFrames to have **compatible schemas** (same number of columns, compatible types).

* **unionByName():** The preferred method. Combines rows based on column **name** rather than position, making it safer for ETL.  
* **intersect():** Returns only rows present in both DFs.  
* **except():** Returns rows in the first DF but not the second (like left\_anti but for entire rows).

## **9\. Window Functions for Complex Analytics**

Window functions perform calculations over a defined set of related rows **without collapsing the rows**.

### **I. Defining the Window Specification**

A window requires three components, defined using the Window object:

1. **Partitioning (partitionBy):** Defines the group (e.g., all rows belonging to a specific user\_id).  
2. **Ordering (orderBy):** Defines the sequence *within* the partition (e.g., order by timestamp).  
3. **Framing (rowsBetween):** Defines the range of rows to include in the calculation (needed for running aggregates).

### **II. Common Window Functions**

* **Ranking:** Requires partitionBy and orderBy.  
  * **row\_number():** Unique, sequential rank (1, 2, 3...).  
  * **dense\_rank():** Ranks with no gaps for ties (1, 2, 2, 3...).  
* **Analytical/Lagging:**  
  * **lag() / lead():** Accesses values from the preceding or succeeding row in the order. Essential for calculating period-over-period differences.  
* **Running Aggregates:** Uses an aggregation function (like sum or avg) combined with framing.  
  \# Running total frame: from the start of the partition to the current row  
  running\_spec \= Window.partitionBy("Store").orderBy("Date").rowsBetween(  
      Window.unboundedPreceding, Window.currentRow  
  )  
  df \= df.withColumn("Run\_Total", F.sum("Sales").over(running\_spec))

## **10\. Spark SQL**

Spark SQL allows declarative querying and is fully integrated with the DataFrame API, leveraging the **Catalyst Optimizer** for efficient execution.

### **I. The Catalyst Optimizer**

This is Spark's query optimization engine. It works by:

1. Parsing the SQL query or DataFrame code.  
2. Creating a logical plan (unoptimized).  
3. Applying optimization rules (e.g., pushdown filters, constant folding).  
4. Creating a physical plan (optimized, runnable code).

### **II. Working with SQL in Databricks**

* **%sql Magic Command:** Executes SQL directly in a Databricks notebook cell.  
* **spark.sql():** Executes a SQL query and returns the result immediately as a DataFrame object in your programmatic code (PySpark/Scala).

### **III. Tables and Views**

SQL queries must operate on named structures:

* **Permanent Tables:** Stored in the Metastore/Unity Catalog, persistent across sessions.  
* **Temporary Views:** Visible only within the current SparkSession.  
  \# Exposing a DataFrame to SQL  
  my\_df.createOrReplaceTempView("v\_temp\_data")

* **Global Temporary Views:** Visible across all sessions on the current cluster (must be queried as global\_temp.view\_name).

## **11\. Introduction to Delta Lake**

Delta Lake is the open-source storage layer that brings ACID properties to the Data Lake, forming the foundation of the Lakehouse.

### **I. Data Lake Limitations Solved by Delta**

* **Lack of Atomicity:** Partial writes or failed jobs left incomplete data.  
* **No Consistency:** Readers saw dirty, in-progress data.  
* **Mutation:** Impossible to efficiently update or delete specific rows.

### **II. The Core: The Transaction Log**

* **Location:** The \_delta\_log subdirectory within the Delta table path.  
* **Content:** A sequence of JSON files that records every change as an **atomic commit** ("Remove file A, Add file B").  
* **ACID Properties:**  
  * **Atomicity:** All changes in a transaction succeed or fail as one unit.  
  * **Consistency:** All readers see a unified, committed view of the data.  
  * **Isolation:** Readers continue to see the old version of the data while a writer is committing a new version (optimistic concurrency).  
  * **Durability:** Once committed, the changes are permanent.

### **III. Basic Delta Operations**

* **Write:** df.write.format("delta").mode("overwrite").save(path)  
* **Read:** spark.read.format("delta").load(path)  
* **Schema Enforcement:** Automatically checks incoming data schema against the table schema and fails writes if incompatible, ensuring data quality.

## **12\. Advanced Delta Lake Features**

Delta Lake enables complex data management operations previously reserved for data warehouses.

### **I. Data Mutation Operations**

These operations perform targeted changes by rewriting only the affected data files.

* **DELETE FROM:** Removes rows matching a predicate.  
* **UPDATE SET:** Modifies column values for rows matching a predicate.  
* **MERGE INTO (Upsert):** The standard operation for ETL. It combines INSERT, UPDATE, and optionally DELETE logic in a single transaction based on a matching key.  
  * **Requirement:** The MERGE operation is essential for implementing **idempotency** in ETL (e.g., updating existing records and inserting new ones).

### **II. Time Travel (Data Versioning)**

The transaction log stores every version of the data, allowing queries against historical states.

* **Query by Version:** spark.read.format("delta").option("versionAsOf", N).load(path)  
* **Query by Timestamp:** spark.read.format("delta").option("timestampAsOf", "YYYY-MM-DD...").load(path)  
* **Rollback:** The RESTORE command creates a new commit that reverts the table's state to a previous version.

### **III. Delta Table Optimization**

Commands used to manage the physical file layout for performance.

* **OPTIMIZE:** Compaction. Combines many small files into fewer, larger files (typically 1GB target size), solving the **Small File Problem**.  
* **ZORDER BY:** Multi-dimensional clustering. Physically co-locates related values across **multiple columns** on disk. This maximizes **Data Skipping** for queries using those columns in filters.

## **13\. Data Ingestion with Auto Loader**

Auto Loader is a Databricks feature for efficient, incremental, and automated ingestion of new data files arriving in cloud storage.

### **I. Auto Loader Operation Modes**

1. **File Notification Mode (Preferred):** Sets up native cloud services (SQS, Event Grid) to push notifications upon file arrival. **Highly scalable and cost-efficient.**  
2. **Directory Listing Mode:** Periodically lists the input directory. Simpler setup but slower and more expensive for directories with millions of files.

### **II. Implementation with Structured Streaming**

Auto Loader is a stream source using the cloudFiles format.

* **Source:** spark.readStream.format("cloudFiles").options(...).load(input\_path)  
* **Checkpoint Location:** A mandatory path that stores the metadata necessary for **idempotency** (tracking processed files) and fault tolerance.

### **III. Schema Evolution**

Auto Loader handles changes in the incoming data schema:

* **failOnNewColumns (Default):** Stops the stream on schema change.  
* **addNewColumns:** Automatically incorporates new columns.  
* **rescue (Recommended for Raw):** Parses records that fail schema validation into a JSON column called \_rescued\_data, ensuring no data loss.

## **14\. Introduction to Structured Streaming**

Spark's engine for continuous data processing, treating the stream as an **Unbounded Table** that is continuously appended to.

### **I. Model: Unbounded Table and Micro-Batches**

* **Unbounded Table:** Allows the use of the familiar **DataFrame API** (select, filter, join) for streaming.  
* **Micro-Batch Processing:** Data is processed in small, discrete batches at regular intervals, providing low-latency, high-throughput results.

### **II. State Management**

* **Stateless Operations:** Performed entirely on the current micro-batch (e.g., filter, select).  
* **Stateful Operations:** Require memory of past micro-batches (e.g., groupBy() aggregation, stream-stream joins).  
  * State is managed and persisted securely in the **Checkpoint Location** for fault tolerance.

### **III. Output Modes**

Defines how the result table is written to the sink in each micro-batch:

* **Append (Default):** Only the new rows appended to the result table are written. (Suitable for simple ingestion/ETL).  
* **Update:** Only rows that have been updated since the last trigger are written. (Suitable for aggregation).  
* **Complete:** The entire, current result table is rewritten every time. (Suitable for small, full aggregations).

## **15\. Streaming Aggregation and Watermarking**

The complexity of streaming aggregations lies in dealing with event time and late-arriving data.

### **I. Time Window Aggregation**

Aggregations must be defined over a **Time Window** based on the event timestamp embedded in the record.

* **window() Function:** Used in the groupBy() clause to create non-overlapping (tumbling) or overlapping (sliding) time buckets.  
  \# Groups by user\_id and non-overlapping 10-minute intervals  
  df.groupBy(window(col("event\_time"), "10 minutes"), col("user\_id")).agg(...)

### **II. Watermarking: State Eviction**

The mechanism to prevent infinite state growth due to late-arriving data.

1. **Define Watermark:** **withWatermark(eventTimeColumn, delayThreshold)**  
   * The delayThreshold specifies how long the stream should wait for late data (e.g., "5 minutes").  
2. **Watermark Calculation:** The Watermark Time is calculated as the **Maximum Event Time seen so far** minus the **Delay Threshold**.  
3. **Eviction:** Any data arriving with an event time older than the Watermark Time is dropped, and the state for the corresponding old windows is evicted from memory.

## **16\. Performance Tuning Fundamentals**

Tuning focuses on minimizing the cost of I/O, network transfer (Shuffle), and CPU usage.

### **I. Identifying Bottlenecks**

The **Spark UI** is the primary diagnostic tool. Look for:

* **High Shuffle Read/Write:** Indicates expensive network I/O.  
* **High Spill (Memory/Disk):** Indicates worker memory exhaustion, forcing data write to local disk (slow).  
* **Data Skew:** Tasks for certain keys take much longer than others (the "long tail").

### **II. Minimizing Shuffles**

* **Broadcast Hash Join (BHJ):** The most effective single optimization (see L8).  
* **Filtering Early:** Apply filter() transformations as early as possible to reduce the amount of data carried through wide transformations.

### **III. Partition Management**

* **repartition(N):** Triggers a **full shuffle** to redistribute data into N partitions. Used to increase parallelism or fix skew.  
* **coalesce(N):** Reduces the number of partitions to N **without a full shuffle**. Used efficiently before writing data to prevent the creation of too many small files.

## **17\. Delta Table Optimization**

Managing the physical structure of the Delta files for maximum query speed.

### **I. File Compaction**

* **OPTIMIZE:** Compaction. Combines many small files into fewer, larger ones (typically 1GB target size), solving the **Small File Problem**. This is a necessary maintenance task for append-heavy tables.

### **II. Data Organization with Z-Ordering**

* **ZORDER BY (col1, col2):** A multi-dimensional clustering algorithm that organizes files so that related values across the specified columns are physically co-located on disk.  
* **Benefit:** Enables maximum **Data Skipping**, as the query engine uses metadata to avoid reading files that cannot possibly contain the filtered data.

### **III. Cleanup**

* **VACUUM:** Permanently removes the underlying data files that are no longer referenced by the transaction log (i.e., files from old versions).  
* **Retention Policy:** Must be run with a safety margin (default 7 days) to ensure time travel queries can still access recent history.

## **18\. Databricks SQL and Data Governance**

### **I. Databricks SQL (DBSQL)**

* **SQL Endpoints (Warehouses):** Dedicated compute clusters optimized for low-latency SQL querying and BI tools. They are separate from ETL clusters, providing workload isolation.  
* **Photon Engine:** A vectorized query engine within DBSQL designed to execute SQL and DataFrame operations extremely fast.

### **II. Unity Catalog (UC)**

The unified governance layer for the Lakehouse.

* **Goal:** Centralized management of security, auditing, and lineage across all data assets.  
* **Three-Level Namespace:** Access data using the familiar structure: catalog.schema.table.  
* **Fine-Grained Security:** Allows access control at the **table, column, and row level** using standard SQL GRANT/REVOKE commands.

### **III. The Medallion Architecture**

A best-practice framework for structuring data quality:

1. **Bronze (Raw):** Untouched, raw data. Full fidelity. Used for history and replayability.  
2. **Silver (Cleaned):** Cleaned, filtered, standardized, and integrated data. Used as the reliable source for analytics.  
3. **Gold (Curated):** Highly aggregated, business-level data optimized for BI reporting and consumption.

## **19\. Designing and Scheduling Data Pipelines**

### **I. Medallion Implementation (Pipeline Flow)**

* **Bronze:** Ingestion via Auto Loader (streaming).  
* **Silver:** Deduplication, Validation, and Transformation (batch or continuous merging).  
* **Gold:** Aggregation, Windowing, and Final Curating (batch for periodic reporting).

### **II. Production Orchestration with Databricks Workflows (Jobs)**

* **Function:** Native tool for scheduling, managing, and monitoring ETL execution.  
* **Structure:** Defines a **DAG (Directed Acyclic Graph)** of tasks (notebooks, SQL files) with dependencies.  
* **Compute:** Uses **Job Clusters**—cost-effective clusters that spin up on demand and terminate immediately after the job finishes.

### **III. Delta Live Tables (DLT)**

A powerful framework for **declarative ETL** that simplifies pipeline development.

* **Declarative Style:** You declare the desired tables and dependencies (dlt.table and dlt.read) rather than writing imperative execution logic.  
* **Automation:** DLT automatically handles dependency ordering, execution retries, schema evolution, and file optimization.  
* **Data Quality:** Define **expectations** (constraints) on table data. DLT can automatically fail the pipeline, drop bad records, or quarantine them for manual inspection.

## **20\. Final Project and Best Practices**

### **I. Code Best Practices**

* **Modularity:** Break pipelines into specialized notebooks/scripts (one for each Medallion layer). Use the %run magic command to import helper functions.  
* **Security:** Store all sensitive information (credentials, tokens) in the **Databricks Secrets Utility** (managed via Unity Catalog).  
* **Cost Management:** Always ensure production jobs are configured to run on **Job Clusters** with Auto-termination enabled.

### **II. Pipeline Example Synthesis**

A fully robust pipeline involves:

1. **Ingestion:** Streaming raw logs (Bronze)  Delta Table.  
2. **Transformation:** Batch processing Silver to resolve identities and clean data.  
3. **Analytics:** Batch processing Gold to aggregate daily metrics.  
4. **Deployment:** Scheduling all three steps in a single **Databricks Workflow** with dependency ordering, ensuring efficient resource use and reliability.