from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.appName("Apartment Price Prediction").getOrCreate()

# Load the dataset
data_path = "https://github.com/msfasha/307401-Big-Data/blob/main/lecture_notes/datasets/apartment_prices.csv"  # Adjust the path if needed
df = spark.read.csv(data_path, header=True, inferSchema=True)

from pyspark.ml.feature import StringIndexer, OneHotEncoder

# Convert the 'City' column to a numeric index
indexer = StringIndexer(inputCol="City", outputCol="CityIndex")
df = indexer.fit(df).transform(df)

# Convert the numeric index to one-hot encoding
encoder = OneHotEncoder(inputCol="CityIndex", outputCol="CityVec")
df = encoder.fit(df).transform(df)

from pyspark.ml.feature import VectorAssembler

# Assemble features into a single vector
assembler = VectorAssembler(inputCols=["Square_Area", "Num_Rooms", "Age_of_Building", "Floor_Level", "CityVec"], outputCol="features")
df = assembler.transform(df)

# Select the final columns for modeling


# Split data into training and test sets
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

from pyspark.ml.regression import LinearRegression

# Initialize Linear Regression model
lr = LinearRegression(featuresCol="features", labelCol="label")

# Train the model on the training data
lr_model = lr.fit(train_data)

# Print model coefficients and intercept
print(f"Coefficients: {lr_model.coefficients}")
print(f"Intercept: {lr_model.intercept}")

from pyspark.ml.evaluation import RegressionEvaluator

# Make predictions on the test data
predictions = lr_model.transform(test_data)

# Show predictions
predictions.select("features", "label", "prediction").show()

# Evaluate model using RMSE
evaluator = RegressionEvaluator(labelCol="label", predictionCol="prediction", metricName="rmse")
rmse = evaluator.evaluate(predictions)
print(f"Root Mean Squared Error (RMSE): {rmse}")

# Initialize RegressionEvaluator with R2 metric
evaluator = RegressionEvaluator(labelCol="label", predictionCol="prediction", metricName="r2")

# Evaluate model using R2
r2 = evaluator.evaluate(predictions)
print(f"R-squared: {r2}")