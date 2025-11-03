### Example 2: Sales Analysis MapReduce

#### Dataset Creation
```bash
# Create sales data
cat << 'EOF' > sales_data.txt
2023-01-01,Electronics,iPhone,999.99,2
2023-01-01,Electronics,Laptop,1299.99,1
2023-01-01,Clothing,Shirt,29.99,3
2023-01-02,Electronics,Mouse,25.99,5
2023-01-02,Books,Python Book,49.99,2
2023-01-02,Clothing,Jeans,79.99,2
2023-01-03,Electronics,Keyboard,89.99,3
2023-01-03,Books,Java Book,59.99,1
EOF

hdfs dfs -put sales_data.txt /user/hadoop/datasets/
```

#### Python MapReduce using MRJob
Create `sales_analysis_mrjob.py`:
```python
#!/usr/bin/env python3
"""
Sales Analysis MapReduce using MRJob
Calculates total revenue by product category
"""

from mrjob.job import MRJob

class MRSalesAnalysis(MRJob):
    
    def mapper(self, _, line):
        # Parse CSV: date,category,product,price,quantity
        line = line.strip()
        if line and not line.startswith('date'):  # Skip header
            fields = line.split(',')
            if len(fields) == 5:
                try:
                    category = fields[1]
                    price = float(fields[3])
                    quantity = int(fields[4])
                    total_sales = price * quantity
                    yield category, total_sales
                except ValueError:
                    pass
    
    def reducer(self, category, sales_values):
        # Sum total sales for each category
        total_revenue = sum(sales_values)
        yield category, round(total_revenue, 2)

if __name__ == '__main__':
    MRSalesAnalysis.run()
```

#### Run the Sales Analysis
```bash
# Test locally
python3 sales_analysis_mrjob.py sales_data.txt

# Run on Hadoop (simple approach)
python3 sales_analysis_mrjob.py -r hadoop hdfs:///user/hadoop/datasets/sales_data.txt > sales_results.txt

# View results
cat sales_results.txt
```

**Step 4: Run on Hadoop**
```bash
# Sales Analysis on Hadoop
echo "=== RUNNING SALES ANALYSIS ON HADOOP ==="
hdfs dfs -rm -r /user/hadoop/output/sales_mrjob

python3 sales_analysis_mrjob.py \
  -r hadoop \
  --hadoop-streaming-jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  --output-dir hdfs:///user/hadoop/output/sales_mrjob \
  hdfs:///user/hadoop/datasets/comprehensive_sales.csv

# Customer Analysis on Hadoop
echo -e "\n=== RUNNING CUSTOMER ANALYSIS ON HADOOP ==="
hdfs dfs -rm -r /user/hadoop/output/customer_mrjob

python3 customer_counter_mrjob.py \
  -r hadoop \
  --hadoop-streaming-jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  --output-dir hdfs:///user/hadoop/output/customer_mrjob \
  hdfs:///user/hadoop/datasets/customer_transactions.txt
```

**Step 5: Analyze Results**
```bash
# View Sales Analysis Results
echo "=== SALES ANALYSIS RESULTS ==="
echo "Category Analysis (Sorted by Revenue):"
hdfs dfs -cat /user/hadoop/output/sales_mrjob/part-00000

# Parse and format the results for better readability
echo -e "\n=== FORMATTED BUSINESS REPORT ==="
hdfs dfs -cat /user/hadoop/output/sales_mrjob/part-00000 | while read line; do
    echo "$line" | tr '\t' '\n' | nl
    echo "---"
done

# View Customer Analysis Results
echo -e "\n=== CUSTOMER ANALYSIS RESULTS ==="
hdfs dfs -cat /user/hadoop/output/customer_mrjob/part-00000

# Generate executive summary
echo -e "\n=== EXECUTIVE SUMMARY ==="
echo "Top Revenue Categories:"
hdfs dfs -cat /user/hadoop/output/sales_mrjob/part-00000 | head -3

echo -e "\nCustomer Engagement Insights:"
hdfs dfs -cat /user/hadoop/output/customer_mrjob/part-00000
```

**Expected Sales Analysis Output:**
```
Electronics	Revenue:$4199.88	Transactions:8	AvgPerTransaction:$524.99	TotalQuantity:16	UniqueProducts:6	AvgPrice:$335.66	TopProducts:Headphones,iPhone,Keyboard,Laptop,Monitor

Clothing	Revenue:$379.94	Transactions:4	AvgPerTransaction:$94.99	TotalQuantity:8	UniqueProducts:4	AvgPrice:$74.99	TopProducts:Jacket,Jeans,Shirt,Sweater

Home	Revenue:$329.96	Transactions:3	AvgPerTransaction:$109.99	TotalQuantity:4	UniqueProducts:3	AvgPrice:$93.32	TopProducts:Blender,Coffee Maker,Microwave
```

**Expected Customer Analysis Output:**
```
High_Activity: 0 customers, 0 total transactions, avg 0.0 transactions per customer. Top customers: 

Low_Activity: 8 customers, 25 total transactions, avg 3.1 transactions per customer. Top customers: C001(7), C002(6), C003(2), C004(1), C005(1)

Medium_Activity: 0 customers, 0 total transactions, avg 0.0 transactions per customer. Top customers: 
```

#### Why MRJob is Superior for Learning

**Advantages of MRJob over traditional Hadoop Streaming:**

1. **Simplicity**: Single file, clean Python syntax
2. **Local Testing**: Debug without cluster setup
3. **Automatic Handling**: No manual mapper/reducer file management
4. **Error Handling**: Better error messages and debugging
5. **Flexibility**: Easy to add multiple steps
6. **Readability**: Code is self-documenting

**Key Learning Points:**

1. **MapReduce Concepts**: Students see the map/reduce pattern clearly
2. **Data Processing**: Real-world business logic examples
3. **Scalability**: Same code works locally and on cluster
4. **Debugging**: Easy to test and troubleshoot
5. **Business Intelligence**: Practical analytics applications

#### Additional MRJob Examples for Practice

**Example 3: Log Analysis**
```python
#!/usr/bin/env python3
"""
Web Log Analysis using MRJob
===========================
Analyze web server logs to find:
- Most visited pages
- Error rates
- Traffic patterns by hour
"""

from mrjob.job import MRJob
import re
from datetime import datetime

class MRLogAnalysis(MRJob):
    
    def mapper(self, _, line):
        # Parse Apache log format
        # Example: 192.168.1.1 - - [01/Jan/2023:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234
        
        log_pattern = r'(\S+) \S+ \S+ \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+) \S+" (\d{3}) (\d+)'
        match = re.match(log_pattern, line)
        
        if match:
            ip, timestamp, method, url, status, size = match.groups()
            
            # Extract hour from timestamp
            try:
                dt = datetime.strptime(timestamp.split()[0], '%d/%b/%Y:%H:%M:%S')
                hour = dt.hour
                
                # Emit different metrics
                yield ('page_visits', url), 1
                yield ('hourly_traffic', hour), 1
                yield ('status_codes', status), 1
                yield ('ip_addresses', ip), 1
                
            except ValueError:
                pass
    
    def reducer(self, key, values):
        metric_type, item = key
        count = sum(values)
        yield f"{metric_type}_{item}", count

if __name__ == '__main__':
    MRLogAnalysis.run()
```

**Example 4: Product Recommendation**
```python
#!/usr/bin/env python3
"""
Product Recommendation using MRJob
==================================
Find products frequently bought together.
"""

from mrjob.job import MRJob
from mrjob.step import MRStep
from itertools import combinations

class MRProductRecommendation(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper_extract_baskets,
                   reducer=self.reducer_find_pairs),
            MRStep(mapper=self.mapper_count_pairs,
                   reducer=self.reducer_recommend)
        ]
    
    def mapper_extract_baskets(self, _, line):
        # Input: customer_id,product1,product2,product3
        if line.strip():
            parts = line.strip().split(',')
            if len(parts) > 2:
                customer = parts[0]
                products = parts[1:]
                
                # Generate all product pairs in this basket
                for pair in combinations(sorted(products), 2):
                    yield pair, 1
    
    def reducer_find_pairs(self, pair, counts):
        total = sum(counts)
        if total >= 2:  # Only pairs bought together at least twice
            yield pair, total
    
    def mapper_count_pairs(self, pair, count):
        product1, product2 = pair
        # Emit both directions for recommendations
        yield product1, (product2, count)
        yield product2, (product1, count)
    
    def reducer_recommend(self, product, recommendations):
        # Sort recommendations by frequency
        recs = sorted(recommendations, key=lambda x: x[1], reverse=True)[:3]
        yield product, [f"{prod}({count})" for prod, count in recs]

if __name__ == '__main__':
    MRProductRecommendation.run()
```

These examples demonstrate the power and simplicity of MRJob for various MapReduce applications, making it much easier for students to understand and implement big data processing solutions!# Hadoop Ecosystem Practical Labs - AWS Academy Sandbox

## Prerequisites and Setup

### 1. Start AWS Academy Lab Environment
1. Access your AWS Academy course
2. Click **Start Lab** to initialize the sandbox
3. Wait for the lab to be ready (green indicator)
4. Click **AWS** to access the AWS Console

### 2. Launch EMR Cluster
```bash
# Navigate to EMR service in AWS Console
# Create cluster with the following settings:
- Name: BigDataTrainingCluster
- Release: emr-6.x.x (latest available)
- Instance type: m5.large (if available, otherwise m4.large)
- Number of instances: 3 (1 master, 2 core)
- EC2 key pair: vockey (create if doesn't exist)
```

### 3. Access Cluster via SSH
```bash
# Get cluster master public DNS from EMR console
# Connect using AWS CloudShell or Cloud9
ssh -i ~/.ssh/id_rsa hadoop@<master-public-dns>
```

---