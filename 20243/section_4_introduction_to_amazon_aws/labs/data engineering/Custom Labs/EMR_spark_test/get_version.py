from pyspark.sql import SparkSession

# Create a Spark session
spark = SparkSession.builder.appName("Introduction to Spark").getOrCreate()

# Display Spark version
print("Spark version:", spark.version)