### **Scenario: Create A vm AND Host a Web Page Using Windows and IIS**

---

### **1. Objective**
In this scenario we will:
1. Create a **Windows Virtual Machine (VM)** on Azure.
2. Install **Internet Information Services (IIS)**.
3. Configure IIS to host a simple web page.
4. Access the hosted web page from a browser.

---

### **2. Prerequisites**
1. **Azure for Students account** with $100 free credits.
2. Access to the **Azure Portal**: [https://portal.azure.com](https://portal.azure.com).
3. A **Remote Desktop Protocol (RDP)** client to connect to the Windows VM (e.g., built-in Remote Desktop Connection on Windows).

---

### **3. Steps**

#### **Step 1: Create a Windows Virtual Machine**

1. **Log in to Azure Portal**:
   - Go to [Azure Portal](https://portal.azure.com) and sign in.

2. **Create a Resource Group**:
   - Navigate to **Resource Groups** > **+ Create**.
   - Name the group (e.g., `windows-vm-project`) and choose a region.

3. **Create the VM**:
   - Navigate to **Virtual Machines** > **+ Create**.
   - Fill in the basic information:
     - **Resource Group**: Select the one you just created.
     - **Virtual Machine Name**: Enter a name (e.g., `windows-vm`).
     - **Region**: Select a region near you.
     - **Image**: Choose **Windows Server 2019 Datacenter** (free tier eligible).
     - **Size**: Select **Standard B1s** (1 vCPU, 1GB RAM).
   - **Administrator Account**:
     - Username: `studentadmin`.
     - Password: Set a strong password.

4. **Configure Inbound Port Rules**:
   - Add the following ports:
     - **RDP (3389)**: For remote desktop access.
     - **HTTP (80)**: To serve the website.

5. **Review + Create**:
   - Review your settings and click **Create**.
   - Wait for the deployment to complete.

---

#### **Step 2: Connect to the VM**

1. **Access the VM**:
   - In the Azure Portal, navigate to the **Overview** tab of the VM.
   - Copy the **Public IP Address**.

2. **Use Remote Desktop**:
   - Open **Remote Desktop Connection** on your local machine.
   - Enter the **Public IP Address** of the VM.
   - Log in using the **username** and **password** you set during VM creation.

---

#### **Step 3: Install IIS (Internet Information Services)**

1. **Open PowerShell**:
   - Once connected to the VM, open **PowerShell** as an administrator.

2. **Install IIS**:
   - Run the following command to install IIS:
     ```powershell
     Install-WindowsFeature -name Web-Server -IncludeManagementTools
     ```

3. **Verify IIS Installation**:
   - Open a web browser on your local machine.
   - Enter the **Public IP Address** of your VM.
   - You should see the default IIS welcome page.

---

#### **Step 4: Host a Web Page**

1. **Access IIS Root Directory**:
   - Open File Explorer on the VM.
   - Navigate to the IIS root directory: `C:\inetpub\wwwroot`.

2. **Replace the Default Page**:
   - Delete the `iisstart.html` file.
   - Create a new `index.html` file with the following content:
     ```html
     <h1>Hello from Azure Windows Virtual Machine</h1>
     ```

3. **Allow HTTP Traffic (Firewall)**:
   - Open PowerShell and run:
     ```powershell
     New-NetFirewallRule -DisplayName "Allow HTTP" -Direction Inbound -Protocol TCP -LocalPort 80 -Action Allow
     ```

4. **Test the Web Page**:
   - Open a browser on your local machine.
   - Enter the **Public IP Address** of your VM.
   - You should see the message: `Hello from Azure Windows Virtual Machine`.

---

#### **Step 5: Optional Enhancements**

1. **Secure the Website with HTTPS**:
   - Install and configure an SSL certificate (e.g., using Let's Encrypt or a self-signed certificate).

2. **Add More Content**:
   - Create additional HTML pages and link them for a mini-website.

3. **Use Azure DNS**:
   - Configure a custom domain to point to the VM’s public IP.

---

### **4. Troubleshooting**

| **Issue**                            | **Solution**                                           |
|--------------------------------------|-------------------------------------------------------|
| Unable to connect via RDP            | Ensure port 3389 is open in **Inbound Port Rules**.   |
| Cannot access the web page           | Ensure port 80 is open and IIS is running.            |
| IIS page shows a "403 Forbidden" error | Verify permissions for the `wwwroot` folder.         |
| Public IP changes on VM restart      | Assign a **Static IP Address** to the VM.            |

---

### **5. Deliverable**
1. Users share:
   - The **Public IP Address** of their VM.
   - A screenshot of their custom web page hosted via IIS.

---

### **6. Learning Outcomes**
|Users will:
- Understand how to create and manage Azure Windows VMs.
- Learn to configure and use IIS for web hosting.
- Gain experience with Windows Server and PowerShell.
- Host a basic static website in a cloud environment.

---

This **Windows and IIS** version is simple yet powerful, giving students hands-on experience with a commonly used web hosting setup in the industry. Let me know if you'd like to expand this scenario!