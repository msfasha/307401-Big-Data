### **Scenario 2: Host a Static Website on Blob Storage**

This scenario teaches users how to use **Azure Blob Storage** to host a static website. It’s a simple, cost-effective solution for deploying static content like HTML, CSS, and JavaScript files without needing a server.

---

### **1. Objective**
Users will:
1. Create a **Blob Storage Account** in Azure.
2. Enable **Static Website Hosting** on the storage account.
3. Upload website files to the Blob Storage container.
4. Access the hosted website via a public endpoint.

---

### **2. Prerequisites**
1. **Azure for Users account** with $100 free credits.
2. A basic static website with:
   - `index.html` (main page).
   - Optional files like CSS, JavaScript, or images.

---

### **3. Steps**

#### **Step 1: Create a Storage Account**
1. **Log in to Azure Portal**:
   - Go to [Azure Portal](https://portal.azure.com) and sign in.

2. **Navigate to Storage Accounts**:
   - Search for **Storage accounts** in the search bar.
   - Click **+ Create**.

3. **Fill in Basic Details**:
   - **Subscription**: Select your subscription.
   - **Resource Group**: Create or select a resource group (e.g., `blob-storage-project`).
   - **Storage Account Name**: Enter a globally unique name (e.g., `studentstorage123`).
   - **Region**: Choose a region close to your location.
   - **Performance**: Select **Standard** (default).
   - **Redundancy**: Choose **Locally Redundant Storage (LRS)** for cost efficiency.

4. **Review and Create**:
   - Click **Review + Create**, then **Create** to deploy the storage account.

---

#### **Step 2: Enable Static Website Hosting**
1. **Access the Storage Account**:
   - In the Azure Portal, go to the newly created storage account.

2. **Enable Static Website Hosting**:
   - In the storage account menu, select **Static website** under **Data management**.
   - Click **Enable**.
   - Specify:
     - **Index document name**: `index.html`.
     - **Error document path**: `404.html` (optional).
   - Click **Save**.

3. **Copy the Public Endpoint**:
   - Once enabled, a **Primary Endpoint** URL is displayed (e.g., `https://studentstorage123.z13.web.core.windows.net`).
   - This is the public URL for the website.

---

#### **Step 3: Create a Blob Container**
1. **Navigate to Containers**:
   - Under the storage account menu, click **Containers**.

2. **Create a Container**:
   - Click **+ Container**.
   - Name the container (e.g., `website-files`).
   - Set **Public Access Level** to **Blob (anonymous read access)**.
   - Click **Create**.

---

#### **Step 4: Upload Website Files**
1. **Open the Container**:
   - Click the newly created container (`website-files`).

2. **Upload Files**:
   - Click **+ Upload**.
   - Select the `index.html` file and other required files (CSS, JavaScript, images).
   - Click **Upload**.

---

#### **Step 5: Test the Website**
1. **Access the Public Endpoint**:
   - Open the **Primary Endpoint URL** in your browser (e.g., `https://studentstorage123.z13.web.core.windows.net`).
2. **Verify the Content**:
   - Ensure your `index.html` is displayed correctly.

---

### **4. Optional Enhancements**

#### **Custom Domain**:
1. Configure a custom domain (e.g., `www.mystudentproject.com`) in **Azure DNS**.
2. Map the custom domain to the Blob Storage endpoint.

#### **Add HTTPS**:
1. Enable HTTPS for secure access to the website.

#### **Host a Portfolio**:
- Users can upload a portfolio website, showcasing their work (e.g., projects, resume).

---

### **5. Troubleshooting**

| **Issue**                                | **Solution**                                                       |
|------------------------------------------|---------------------------------------------------------------------|
| Website doesn't load                     | Ensure `index.html` is uploaded and matches the static website configuration. |
| Error accessing files                    | Verify that the container's **Public Access Level** is set to **Blob**. |
| Changes to the website aren’t reflected  | Clear browser cache or refresh the page.                           |
| Cannot find static website settings      | Confirm that the storage account was created with **General-purpose v2** tier. |

---

### **6. Deliverable**
Users should:
1. Share the **Primary Endpoint URL** of their static website.
2. Provide screenshots of their hosted webpage in a browser.

---

### **7. Learning Outcomes**
Users will:
- Understand how to create and manage Azure Blob Storage.
- Learn to enable and configure static website hosting.
- Deploy a live website in the cloud.
- Experience a serverless hosting model.

---

This scenario is simple, cost-effective, and gives users hands-on experience with serverless web hosting in Azure. Let me know if you’d like further guidance or additional enhancements for this project!