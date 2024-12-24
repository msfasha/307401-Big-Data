### **Scenario: Create a Data Lake in Azure**

---

### **1. Objective**

In this scenario, you will learn how to:
1. Create an **Azure Data Lake Storage Gen2** account, a powerful and scalable cloud storage service for big data analytics.
2. Organize data using **containers and directories**, which function like folders for storing and managing files.
3. Upload sample data to the Data Lake for use in analytics.
4. Access and query the data using Azure tools.

---

### **2. Prerequisites**
1. An **Azure for Students account** with free credits.
2. Access to the **Azure Portal**: [https://portal.azure.com](https://portal.azure.com).
3. Basic understanding of file systems and cloud storage concepts.

---

### **3. Overview of Key Components**

#### **What is a Storage Account?**
- A **Storage Account** is a container for storing all your Azure storage data, including blobs (binary large objects), files, queues, and tables.
- It provides scalable, secure, and highly available storage for a wide range of use cases like big data, website hosting, and backups.

#### **What are Containers and Directories?**
- **Containers**: Containers are like top-level folders within a storage account. They group and organize your files. Think of them as "buckets" where data is stored securely.
- **Directories**: Inside a container, you can create **directories**, which are like subfolders, to further organize your files.

---

### **4. Steps to Create a Data Lake**

#### **Step 1: Create a Data Lake Storage Account**

1. **Log in to Azure Portal**:
   - Visit [Azure Portal](https://portal.azure.com) and sign in to your account.

2. **Create a Resource Group**:
   - A **Resource Group** is a logical container for managing related Azure resources.
   - Navigate to **Resource Groups** > **+ Create**.
   - Provide a name for the group (e.g., `data-lake-project`) and choose a region (e.g., East US).

3. **Create a Storage Account**:
   - Navigate to **Storage Accounts** > **+ Create**.
   - Fill in the following details:
     - **Resource Group**: Select the one you just created.
     - **Storage Account Name**: Enter a globally unique name (e.g., `mystudentdatalake`).
     - **Region**: Choose a region close to your location.
     - **Performance**: Standard (suitable for most use cases).
     - **Redundancy**: Locally Redundant Storage (LRS), which keeps multiple copies of your data within the same region.
   - Enable **Hierarchical Namespace** under the **Advanced** tab. This allows the storage account to function as a **Data Lake** for managing files and directories.
   - Click **Review + Create** and wait for the deployment to complete.

---

#### **Step 2: Create Containers and Directories**

1. **Navigate to Containers**:
   - In the storage account, go to **Containers** > **+ Container**.
   - Containers serve as the top-level grouping mechanism for your files.

2. **Create a Container**:
   - Provide a name for the container (e.g., `raw-data`) and set the **Public Access Level** to `Private` to ensure secure access.

3. **Organize Data with Directories**:
   - Open the `raw-data` container and click **+ Add Directory**.
   - Create subfolders such as `sales`, `marketing`, and `hr`. These directories will help categorize your data based on its source or purpose.

---

#### **Step 3: Upload Sample Data**

1. **Prepare Sample Data**:
   - Create or download simple text or CSV files for each directory, such as:
     - `sales/sales-data.csv`
     - `marketing/marketing-data.csv`

2. **Upload Files**:
   - Navigate to each directory in your container.
   - Click **Upload**, select the file for that directory, and complete the upload.

---

#### **Step 4: Access and Query the Data**

1. **Use Azure Storage Explorer** (optional):
   - Download [Azure Storage Explorer](https://azure.microsoft.com/en-us/features/storage-explorer/).
   - Sign in to your Azure account and view your storage account and its contents.
   - This tool provides an easy way to manage your files locally without using the Azure Portal.

2. **Query Data Using Azure Synapse Studio**:
   - Navigate to **Azure Synapse Analytics** > **+ Create** to create a workspace.
   - Link the Synapse workspace to your Data Lake Storage account.
   - Use the built-in **serverless SQL pool** to query the files directly using SQL commands, turning raw data into valuable insights.

---

### **5. Troubleshooting**

| **Issue**                            | **Solution**                                           |
|--------------------------------------|-------------------------------------------------------|
| Unable to access the storage account | Verify your Azure permissions and account settings.   |
| Cannot upload files                  | Ensure the container and directories exist.           |
| Access denied when querying data     | Check Synapse workspace permissions and configurations. |

---

### **6. Deliverable**
1. Provide:
   - The **Storage Account Name**.
   - A screenshot showing your **Data Lake structure** with containers, directories, and uploaded files.
   - Screenshots of your SQL queries and results (if Synapse Studio is used).

---

### **7. Learning Outcomes**
By completing this scenario, you will:
- Understand how to set up and use Azure Data Lake Storage for big data.
- Learn the difference between storage accounts, containers, and directories.
- Gain hands-on experience uploading and organizing data.
- Explore basic analytics using Azure Synapse Studio.

---
