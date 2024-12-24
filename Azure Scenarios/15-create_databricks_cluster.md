### **Scenario: Create a Databricks Cluster in Azure**

---
### **1. Introduction to Azure Databricks**

- Azure Databricks is a powerful, cloud-based analytics service that brings together the scalability of Apache Spark with the seamless integration of Azure’s ecosystem.
- It is Designed for big data processing, machine learning, and AI development, Azure Databricks provides a collaborative environment where data engineers, data scientists, and business analysts can work together efficiently.

- By leveraging Azure Databricks, organizations can process massive datasets, build advanced data pipelines, and deploy machine learning models—all within a secure and highly scalable platform. 
- Its user-friendly interface, integration with popular programming languages, and compatibility with Azure services make it an essential tool for modern data-driven applications.

#### **Key Features of Azure Databricks**

<div style="text-align: center;">
    <img src="https://raw.githubusercontent.com/msfasha/307304-Data-Mining/main/images/kmeans-1.png" alt="KMeans Algorithm" width="600"/>
</div>

a. **Unified Analytics Platform**:  
   Azure Databricks simplifies workflows by unifying data engineering, data analysis, and AI tasks in a single platform.

b. **Managed Apache Spark**:  
   As a managed service, Azure Databricks handles the complexities of Spark cluster management, allowing users to focus on their data instead of infrastructure.

c. **Collaboration Tools**:  
   With interactive notebooks, teams can work together in real time, using Python, SQL, Scala, or R, to write and test code collaboratively.

d. **Seamless Azure Integration**:  
   Azure Databricks integrates with Azure services like Azure Data Lake, Azure Blob Storage, Azure Synapse Analytics, and Azure Machine Learning to provide end-to-end solutions.

e. **Enterprise-Grade Security**:  
   Built on Azure’s secure infrastructure, the service includes features such as Azure Active Directory (AAD) integration, role-based access control (RBAC), and encryption for data protection.

f. **Scalability and Performance**:  
   With auto-scaling clusters, Azure Databricks adjusts resources dynamically to match workload demands, ensuring optimal performance and cost efficiency.

#### **Capabilities of Azure Databricks**

a. **Big Data Processing**:  
   Process and analyze vast datasets efficiently with Apache Spark’s distributed computing engine.

b. **Machine Learning**:  
   Build, train, and deploy AI models using frameworks like TensorFlow, PyTorch, and MLlib, and integrate seamlessly with Azure Machine Learning.

c. **Stream Processing**:  
   Analyze real-time data streams for applications such as IoT, fraud detection, and dynamic pricing.

d. **SQL Analytics**:  
   Use SQL for querying and transforming structured and semi-structured data, making it accessible to data analysts and BI tools.

e. **Interactive Visualizations**:  
   Create visual dashboards and reports directly within Databricks, or integrate with tools like Power BI for advanced business insights.

Azure Databricks provides a robust platform for modern analytics and AI workloads, empowering organizations to unlock the full potential of their data while leveraging the power and reliability of Microsoft Azure.

---

### 2. Create Databricks Workspace in Azure

### **Prerequisites**

a. **Azure for Students account** with $100 free credits.
b. Access to the **Azure Portal**: [https://portal.azure.com](https://portal.azure.com).
c. Basic understanding of **big data concepts** and familiarity with **Apache Spark**.

---

### **Steps**

#### **Step 1: Create a Databricks Workspace**

a. **Log in to Azure Portal**:
   - Go to [Azure Portal](https://portal.azure.com) and sign in.

b. **Create a Resource Group**:
   - Navigate to **Resource Groups** > **+ Create**.
   - Name the group (e.g., `databricks-project`) and choose a region.

c. **Create the Databricks Workspace**:
   - Navigate to **Create a Resource** and search for **Azure Databricks**.
   - Select **Azure Databricks** and click **Create**.
   - Fill in the workspace details:
     - **Resource Group**: Select the one you just created.
     - **Workspace Name**: Enter a name (e.g., `databricks-workspace`).
     - **Region**: Choose a location close to you.
     - **Pricing Tier**: Select **Standard** (free tier if eligible).

d. **Review + Create**:
   - Review your settings and click **Create**.
   - Wait for the deployment to complete.

e. **Access the Workspace**:
   - Once the deployment is complete, go to the **Resource** and click **Launch Workspace** to open the Databricks environment.

---

#### **Step 2: Configure and Start a Cluster**

a. **Navigate to Clusters**:
   - In the Databricks workspace, click on the **Clusters** tab from the left-hand menu.

b. **Create a New Cluster**:
   - Click **Create Cluster** and fill in the details:
     - **Cluster Name**: Give it a name (e.g., `learning-cluster`).
     - **Cluster Mode**: Choose **Single Node** for simplicity (or **Standard** for distributed mode).
     - **Databricks Runtime Version**: Choose the latest LTS (e.g., **11.x LTS**).
     - **Autoscaling**: Enable or disable based on your preference.
     - **Worker Node Size**: Select **Standard_DS3_v2** (2 vCPUs, 7GB RAM).

c. **Launch the Cluster**:
   - Click **Create Cluster** and wait for it to start. This may take a few minutes.

---

#### **Step 3: Explore the Databricks Interface**

a. **Home Page**:
   - Familiarize yourself with the interface, including **Workspace**, **Clusters**, **Jobs**, and **Data** tabs.

b. **Create a Notebook**:
   - Navigate to the **Workspace** tab.
   - Right-click on your user folder, select **Create** > **Notebook**.
   - Name the notebook (e.g., `test-notebook`) and set the default language to **Python**.

---

#### **Step 4: Run a Simple Notebook**

a. **Write a Simple Spark Job**:
   - In the notebook, enter the following code:
     ```python
     # Create a DataFrame
     data = [("Mohammed", "BI"), ("Ali", "Data Science"), ("Sara", "AI")]
     columns = ["Name", "Specialization"]
     df = spark.createDataFrame(data, columns)

     # Show the DataFrame
     df.show()
     ```

b. **Attach the Notebook to the Cluster**:
   - At the top of the notebook, click **Detached** and select your cluster.

c. **Run the Code**:
   - Press **Shift + Enter** or click the **Run** icon next to the cell.
   - The output should display the data as a table.
