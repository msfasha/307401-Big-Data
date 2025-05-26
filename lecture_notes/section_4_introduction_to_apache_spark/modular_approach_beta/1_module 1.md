# Module 1: Spark Foundations
**Duration:** 2 weeks | **Environment:** Google Colab

## **Week 1: Introduction to Apache Spark**

### **Day 1-2: Big Data & Distributed Computing Fundamentals**

**Learning Objectives:**
- Understand the challenges of processing large datasets
- Grasp the concept of distributed computing
- Identify when to use Spark vs traditional tools

**Content:**

**The Big Data Problem:**
Traditional data processing tools like pandas work great for datasets that fit in memory, but what happens when you have terabytes of data? Consider a telecommunications company processing call records - millions of records per hour across thousands of cell towers. A single machine simply cannot handle this volume efficiently.

**Distributed Computing Solutions:**
Instead of buying one massive computer, distributed systems use many commodity machines working together. Think of it like a restaurant kitchen - instead of one super-chef doing everything, you have specialized stations (prep, grill, dessert) working in parallel.

**Why Apache Spark?**
Spark emerged to solve the limitations of earlier big data tools like MapReduce:
- **Speed:** In-memory processing (up to 100x faster than Hadoop MapReduce)
- **Ease of use:** High-level APIs in Python, Scala, Java, R
- **Unified platform:** Batch processing, streaming, machine learning, graph processing

**Practical Exercise 1:** Setting up Spark in Google Colab
```python
# Install PySpark
!pip install pyspark

# Create SparkSession
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("SparkFoundations").getOrCreate()

# Verify installation
print(f"Spark version: {spark.version}")
print(f"Available cores: {spark.sparkContext.defaultParallelism}")
```

### **Day 3-4: Spark Architecture Deep Dive**

**The Spark Ecosystem:**
Spark isn't just one tool - it's a unified analytics engine with multiple components:
- **Spark Core:** The foundation providing distributed task dispatching and scheduling
- **Spark SQL:** For working with structured data using SQL queries
- **MLlib:** Machine learning library with algorithms and utilities
- **GraphX:** For graph processing and analysis
- **Structured Streaming:** For real-time data processing

**Driver vs Executors:**
Understanding Spark's architecture is crucial for effective programming:

**Driver Program:** The main control unit that:
- Contains your application's main function
- Creates the SparkContext
- Converts your program into tasks
- Schedules tasks across executors

**Executors:** Worker nodes that:
- Run the actual computations
- Store data in memory for caching
- Return results to the driver

**Practical Exercise 2:** Understanding the Architecture
```python
# Check current configuration
print("Driver memory:", spark.conf.get("spark.driver.memory"))
print("Executor memory:", spark.conf.get("spark.executor.memory"))
print("Number of executor cores:", spark.conf.get("spark.executor.cores"))

# Create sample data to see parallelization
data = list(range(1, 1000001))  # 1 million numbers
rdd = spark.sparkContext.parallelize(data, numSlices=4)
print(f"Number of partitions: {rdd.getNumPartitions()}")
```

## **Week 2: RDDs, DataFrames, and Core Concepts**

### **Day 5-6: Resilient Distributed Datasets (RDDs)**

**What are RDDs?**
RDDs are Spark's fundamental data structure - think of them as distributed collections that can be processed in parallel across a cluster. They're "resilient" because they can recover from node failures by recomputing lost partitions.

**Key RDD Characteristics:**
- **Immutable:** Once created, they cannot be changed
- **Partitioned:** Data is divided across multiple nodes
- **Fault-tolerant:** Can rebuild lost data using lineage information
- **Lazy evaluation:** Transformations aren't executed until an action is called

**Transformations vs Actions:**
This is a crucial concept that confuses many beginners:

**Transformations** (lazy - return new RDDs):
- `map()`, `filter()`, `flatMap()`, `groupBy()`
- Nothing happens until an action is called

**Actions** (eager - trigger computation):
- `collect()`, `count()`, `first()`, `saveAsTextFile()`
- These actually execute the computation

**Practical Exercise 3:** Working with RDDs
```python
# Create RDD from list
numbers = spark.sparkContext.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Transformations (lazy)
even_numbers = numbers.filter(lambda x: x % 2 == 0)
squared = even_numbers.map(lambda x: x ** 2)

# Action (triggers execution)
result = squared.collect()
print("Even numbers squared:", result)

# Demonstrate lazy evaluation
print("Before action - no computation happened yet")
count = squared.count()  # This triggers the entire chain
print(f"Count of even squared numbers: {count}")
```

### **Day 7-8: DataFrames - The Modern Approach**

**Why DataFrames Over RDDs?**
While RDDs are powerful, DataFrames offer significant advantages:
- **Optimization:** Catalyst optimizer automatically optimizes queries
- **Easier syntax:** More intuitive, SQL-like operations
- **Better performance:** Optimized execution plans
- **Schema enforcement:** Structured data with defined types

**DataFrame vs Pandas DataFrame:**
Spark DataFrames are distributed and can handle data larger than memory, while Pandas DataFrames are limited to single-machine memory.

**Practical Exercise 4:** DataFrame Fundamentals
```python
# Create DataFrame from data
data = [("Alice", 25, "Engineer"), 
        ("Bob", 30, "Manager"), 
        ("Charlie", 35, "Analyst")]
columns = ["Name", "Age", "Role"]

df = spark.createDataFrame(data, columns)

# Basic operations
df.show()
df.printSchema()
print(f"Number of rows: {df.count()}")

# Filtering and selecting
young_engineers = df.filter((df.Age < 30) & (df.Role == "Engineer"))
young_engineers.show()

# SQL-style operations
df.createOrReplaceTempView("employees")
result = spark.sql("SELECT Name, Age FROM employees WHERE Age > 25")
result.show()
```

### **Day 9-10: Hands-on Project & Performance Concepts**

**Understanding Partitioning:**
Partitioning determines how data is distributed across the cluster. Good partitioning is crucial for performance.

**Caching and Persistence:**
When you'll use the same dataset multiple times, caching it in memory can dramatically improve performance.

**Practical Exercise 5:** Real Dataset Processing
```python
# Create a larger dataset for demonstration
import random
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Generate sample sales data
def generate_sales_data(n=100000):
    products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]
    regions = ["North", "South", "East", "West", "Central"]
    
    data = []
    for i in range(n):
        data.append((
            f"TXN{i:06d}",
            random.choice(products),
            random.choice(regions),
            random.randint(1, 10),
            round(random.uniform(100, 2000), 2)
        ))
    return data

# Create schema
schema = StructType([
    StructField("transaction_id", StringType(), True),
    StructField("product", StringType(), True),
    StructField("region", StringType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("price", DoubleType(), True)
])

# Generate and create DataFrame
sales_data = generate_sales_data(100000)
sales_df = spark.createDataFrame(sales_data, schema)

# Cache for multiple operations
sales_df.cache()

# Analysis operations
print("=== Sales Analysis ===")
print(f"Total transactions: {sales_df.count()}")

# Sales by region
print("\n=== Sales by Region ===")
sales_df.groupBy("region").sum("price").orderBy("sum(price)", ascending=False).show()

# Top products
print("\n=== Top Products by Revenue ===")
sales_df.groupBy("product").sum("price").orderBy("sum(price)", ascending=False).show()

# Performance comparison
import time

# Without caching
sales_df_no_cache = spark.createDataFrame(sales_data, schema)

start_time = time.time()
result1 = sales_df_no_cache.count()
result2 = sales_df_no_cache.groupBy("region").count().collect()
no_cache_time = time.time() - start_time

# With caching
start_time = time.time()
result1 = sales_df.count()
result2 = sales_df.groupBy("region").count().collect()
cache_time = time.time() - start_time

print(f"\nPerformance Comparison:")
print(f"Without caching: {no_cache_time:.2f} seconds")
print(f"With caching: {cache_time:.2f} seconds")
print(f"Speedup: {no_cache_time/cache_time:.2f}x")
```

## **Assessment for Module 1**

**Assignment 1:**
1. Set up Spark in their own Colab environment
2. Create a DataFrame from a provided CSV dataset
3. Perform basic analysis (filtering, grouping, aggregation)
4. Compare performance with and without caching
5. Write a brief report explaining RDD vs DataFrame trade-offs

**Key Concepts to Master:**
- Spark architecture (driver/executor model)
- Lazy evaluation and the difference between transformations and actions
- When to use RDDs vs DataFrames
- Basic performance optimization through caching and partitioning

**Common Pitfalls to Address:**
- Calling `.collect()` on large datasets (brings all data to driver)
- Not understanding lazy evaluation
- Forgetting to cache frequently accessed datasets
- Misunderstanding the distributed nature of Spark operations