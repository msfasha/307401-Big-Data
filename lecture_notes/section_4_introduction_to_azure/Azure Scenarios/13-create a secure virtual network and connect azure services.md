### **Scenario 13: Create a Secure Virtual Network and Connect Azure Services**

This scenario introduces users to creating a secure **Azure Virtual Network (VNet)**, connecting multiple Azure resources like Virtual Machines and Azure SQL Database within the VNet, and setting up secure access with **Network Security Groups (NSGs)**.

---

### **1. Objective**
Users will:
1. Create a **Virtual Network (VNet)** in Azure.
2. Set up subnets and deploy resources like VMs and Azure SQL Database into the VNet.
3. Configure **Network Security Groups (NSGs)** for secure access.
4. Test connectivity between resources within the VNet.

---

### **2. Prerequisites**
1. **Azure for Students account** with $100 free credits.
2. Basic knowledge of Azure services like VMs and Azure SQL Database.

---

### **3. Steps**

#### **Step 1: Create a Virtual Network**

1. **Log in to Azure Portal**:
   - Go to [Azure Portal](https://portal.azure.com) and sign in.

2. **Navigate to Virtual Networks**:
   - Search for **Virtual Networks** in the search bar and click **+ Create**.

3. **Fill in Basic Details**:
   - **Resource Group**: Create or select an existing group (e.g., `secure-vnet-group`).
   - **Name**: Enter a name for the VNet (e.g., `user-secure-vnet`).
   - **Region**: Select a region close to you.

4. **Configure IP Addresses**:
   - Under **IP Addresses**, define the address space (e.g., `10.1.0.0/16`).
   - Create subnets:
     - **Subnet 1**: Name: `app-subnet`, Address range: `10.1.1.0/24`.
     - **Subnet 2**: Name: `db-subnet`, Address range: `10.1.2.0/24`.

5. **Add Security Configurations**:
   - Leave **DDoS Protection** as Basic.
   - Proceed without enabling a firewall for now.

6. **Review and Create**:
   - Click **Review + Create**, then **Create**.

---

#### **Step 2: Deploy Resources into the VNet**

##### **A. Deploy a Virtual Machine**
1. Navigate to **Virtual Machines** and click **+ Create**.
2. Fill in the details:
   - **Name**: `app-vm`.
   - **Resource Group**: Select the same group as the VNet.
   - **Region**: Ensure it matches the VNet region.
   - **Image**: Select **Ubuntu Server 20.04 LTS** or **Windows Server**.
   - **Size**: Choose a free tier-eligible size (e.g., Standard_B1s).
3. **Network Settings**:
   - Under the **Networking** tab, attach the VM to the `app-subnet`.
   - Set **Public IP** to **None** (for internal use only).

4. **Review and Create**:
   - Click **Review + Create**, then **Create**.

##### **B. Deploy an Azure SQL Database**
1. Navigate to **Azure SQL** and click **+ Create SQL Database**.
2. Fill in the details:
   - **Database Name**: `user-database`.
   - **Server**: Create a new server with a private IP (e.g., `user-sql-server`).
   - **Resource Group**: Select the same group.
   - **Region**: Ensure it matches the VNet region.

3. **Network Configuration**:
   - Under the **Networking** tab, enable **Private Endpoint** and link it to the `db-subnet`.

4. **Review and Create**:
   - Click **Review + Create**, then **Create**.

---

#### **Step 3: Configure Network Security**

##### **A. Set Up Network Security Groups**
1. **Navigate to NSGs**:
   - In the Azure Portal, search for **Network Security Groups** and click **+ Create**.

2. **Create NSGs for Subnets**:
   - **App Subnet NSG**:
     - Name: `app-nsg`.
     - Attach to the `app-subnet`.
   - **DB Subnet NSG**:
     - Name: `db-nsg`.
     - Attach to the `db-subnet`.

3. **Add Inbound Security Rules**:
   - For `app-nsg`:
     - Allow SSH/RDP (port 22 for Linux, port 3389 for Windows) from your local machine's IP.
     - Allow internal traffic from `10.1.0.0/16` (VNet address space).
   - For `db-nsg`:
     - Allow SQL traffic (port 1433) from the `app-subnet`.

4. **Add Outbound Security Rules**:
   - Leave default outbound rules for internet access (if needed).

---

#### **Step 4: Test Connectivity**

1. **Connect to the VM**:
   - SSH or RDP into the `app-vm` using the private IP of the VM.

2. **Install a Database Client**:
   - On the VM, install a database client (e.g., `mysql-client` or `sqlcmd`).
     - Example for Ubuntu:
       ```bash
       sudo apt update
       sudo apt install mysql-client
       ```

3. **Test Database Connection**:
   - Use the private IP of the Azure SQL Database's private endpoint:
     ```bash
     mysql -h <private-sql-endpoint-ip> -u <username> -p
     ```

4. **Verify Communication**:
   - Ensure you can query the database from the VM.

---

### **4. Optional Enhancements**

#### **Enable Azure Firewall**
- Add an Azure Firewall to the VNet to control outbound and inbound traffic more granularly.

#### **Set Up Bastion Host**
- Deploy an Azure Bastion host for secure, browser-based SSH or RDP access to the VM without a public IP.

#### **Add Diagnostics**
- Enable Network Watcher for monitoring network activity and troubleshooting connectivity issues.

#### **Integrate with Private DNS**
- Set up private DNS zones to resolve private endpoint names within the VNet.

---

### **5. Troubleshooting**

| **Issue**                                | **Solution**                                                      |
|------------------------------------------|--------------------------------------------------------------------|
| Unable to SSH/RDP into the VM            | Verify NSG rules and ensure your local IP is whitelisted.          |
| Cannot connect to Azure SQL Database     | Check the private endpoint connection and NSG rules.               |
| VM cannot communicate with database      | Ensure the VM is in the `app-subnet` and NSG rules allow traffic.  |
| Incorrect IP configuration               | Verify the subnet and VNet address space.                         |

---

### **6. Deliverable**
Users should:
1. Provide a screenshot showing successful connection from the VM to the SQL database.
2. Share details of the VNet configuration (e.g., subnets, NSGs).

---

### **7. Learning Outcomes**
Users will:
- Understand how to create and manage a **Virtual Network (VNet)** in Azure.
- Configure secure communication between Azure resources.
- Learn to use **Network Security Groups (NSGs)** for access control.
- Gain practical experience with private endpoints and secure networking.

---

This project equips users with foundational skills in Azure networking and secure communication between resources.