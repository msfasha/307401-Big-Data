from pyspark import SparkContext
import numpy as np

def main():
    # Step 1: Generate a random array of 50 million customer IDs between 1 and 10000
    customer_ids = np.random.randint(1, 10001, size=50_000_000)
    
    # Save the customer IDs to a text file for PySpark to read
    np.savetxt("customer_ids.txt", customer_ids, fmt='%d')
    
    # Create a Spark context
    sc = SparkContext("local[*]", "CustomerIDCount")

    # Step 2: Load the customer IDs from the text file
    customer_id_rdd = sc.textFile("customer_ids.txt")

    # Step 3: Map phase - create pairs of (customer_id, 1)
    counts_rdd = customer_id_rdd.map(lambda x: (x, 1))

    # Step 4: Reduce phase - sum the counts for each customer ID
    result_rdd = counts_rdd.reduceByKey(lambda a, b: a + b)

    # Collect and print results
    results = result_rdd.collect()
    for customer_id, count in results:
        print(f"Customer ID: {customer_id}, Count: {count}")

    # Stop the Spark context
    sc.stop()

if __name__ == "__main__":
    main()
