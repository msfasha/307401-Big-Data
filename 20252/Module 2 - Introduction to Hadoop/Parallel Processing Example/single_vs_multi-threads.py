import os
from multiprocessing import Pool, cpu_count
import numpy as np
import time
from datetime import datetime, timedelta

# Function to count IDs in a chunk (used in both single and multi-process)
def count_chunk(chunk):
    counts = {}
    for customer_id in chunk:
        if customer_id in counts:
            counts[customer_id] += 1
        else:
            counts[customer_id] = 1
    return counts

# Function to count customer IDs without multiprocessing (single process)
def count_ids_single_process(customer_ids):
    return count_chunk(customer_ids)

# Function to count customer IDs with multiprocessing
def count_ids_multiprocess(customer_ids):
    num_processes = cpu_count()  # Get the number of available CPU cores
    print(f"Number of CPU cores detected: {num_processes}")

    chunk_size = len(customer_ids) // num_processes
    chunks = []
    for i in range(num_processes):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i < num_processes - 1 else len(customer_ids)
        chunks.append(customer_ids[start_index:end_index])

    with Pool(num_processes) as pool:
        results = pool.map(count_chunk, chunks)

    # Combine the results from all processes
    total_count = {}
    for result in results:
        for key, value in result.items():
            if key in total_count:
                total_count[key] += value
            else:
                total_count[key] = value
    
    return total_count

if __name__ == "__main__":
    # Step 1: Generate a random array of 50 million customer IDs between 1 and 10000
    print("Generating 50,000,000 random customer IDs...\n")
    customer_ids = np.random.randint(1, 10001, size=50_000_000)

    # Measure the time for single-process counting
    start_time_single = time.time()
    print("Counting customer IDs using single process...")
    print(f"start_time_single: {datetime.fromtimestamp(start_time_single):%H:%M:%S}")
    single_process_result = count_ids_single_process(customer_ids)
    end_time_single = time.time()
    single_process_duration = end_time_single - start_time_single
    print(f"end_time_single: {datetime.fromtimestamp(end_time_single):%H:%M:%S}")
    print(f"single_process_duration: {timedelta(seconds=single_process_duration)}\n\n")


    # Measure the time for multi-process counting
    print("Counting customer IDs using multi-process...")    
    start_time_multi = time.time()
    print(f"start_time_multi: {datetime.fromtimestamp(start_time_multi):%H:%M:%S}")
    multi_process_result = count_ids_multiprocess(customer_ids)
    end_time_multi = time.time()
    print(f"end_time_multi: {datetime.fromtimestamp(end_time_multi):%H:%M:%S}")

    multi_process_duration = end_time_multi - start_time_multi
    print(f"Multi-process duration (using {cpu_count()} cores): {timedelta(seconds=multi_process_duration)}\n")

    
