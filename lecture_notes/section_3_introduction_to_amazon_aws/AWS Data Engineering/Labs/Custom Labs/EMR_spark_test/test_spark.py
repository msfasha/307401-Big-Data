from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("TestJob").getOrCreate()
data = spark.range(1, 100).toDF("number")
data.show()
spark.stop()
