### **Scenario 12: Implement Data Backup and Restore with Azure Recovery Services**

This scenario introduces users to using **Azure Recovery Services** to back up and restore data for virtual machines, databases, and file systems in Azure.

---

### **1. Objective**
Users will:
1. Create an **Azure Recovery Services Vault**.
2. Configure backup for an Azure Virtual Machine (VM).
3. Restore the VM from the backup.

---

### **2. Prerequisites**
1. **Azure for Students account** with $100 free credits.
2. An **Azure Virtual Machine** (Windows or Linux) already set up.
3. Basic knowledge of Azure Portal.

---

### **3. Steps**

#### **Step 1: Create a Recovery Services Vault**

1. **Log in to Azure Portal**:
   - Go to [Azure Portal](https://portal.azure.com) and sign in.

2. **Navigate to Recovery Services Vaults**:
   - Search for **Recovery Services Vaults** in the search bar and click **+ Create**.

3. **Fill in Basic Details**:
   - **Resource Group**: Select or create a new resource group (e.g., `backup-project`).
   - **Vault Name**: Enter a unique name (e.g., `user-backup-vault`).
   - **Region**: Choose the same region as your VM.

4. **Review and Create**:
   - Click **Review + Create**, then **Create**.

---

#### **Step 2: Configure Backup for a Virtual Machine**

1. **Navigate to the Recovery Services Vault**:
   - Go to the created vault in the Azure Portal.

2. **Set Up Backup**:
   - In the vault's menu, select **Backup**.
   - **Where is your workload running?**: Choose **Azure**.
   - **What do you want to back up?**: Select **Azure Virtual Machine**.
   - Click **Backup**.

3. **Select the VM**:
   - In the **Backup Goal** section, click **Add Items** and select the VM(s) you want to back up.

4. **Configure Backup Policy**:
   - Use the default policy or create a custom one:
     - **Backup Frequency**: Daily or Weekly.
     - **Retention Range**: Specify how long backups should be retained.
   - Save the policy.

5. **Enable Backup**:
   - Click **Enable Backup** to start protecting the selected VM.

---

#### **Step 3: Trigger a Backup Job**

1. **Initiate Backup**:
   - Go to the **Backup Items** section in the vault.
   - Select **Azure Virtual Machine** and locate your VM.
   - Click **Backup Now** to create the first backup.

2. **Monitor the Backup Job**:
   - Go to **Backup Jobs** under the vault to monitor the progress.
   - Once the backup is complete, you’ll see it listed in the **Recovery Points** section.

---

#### **Step 4: Restore the Virtual Machine**

1. **Initiate Restore**:
   - In the Recovery Services Vault, go to **Backup Items** > **Azure Virtual Machine**.
   - Select the VM you want to restore.
   - Click **Restore VM**.

2. **Choose a Recovery Point**:
   - Select the backup point you want to restore from.

3. **Restore Configuration**:
   - **Restore Type**:
     - **Create New VM**: Creates a new VM from the backup.
     - **Replace Existing VM**: Replaces the current VM (use with caution).
   - Configure VM settings (e.g., name, resource group, virtual network).

4. **Start the Restore Job**:
   - Click **OK** to start the restore process.
   - Monitor the restore job under **Backup Jobs**.

5. **Verify the Restored VM**:
   - Once the restore is complete, navigate to the restored VM and ensure it is running correctly.

---

### **4. Optional Enhancements**

#### **Backup for Azure Files or SQL Databases**:
- Use Azure Recovery Services Vault to back up Azure SQL Databases or Azure Files.

#### **Long-Term Retention**:
- Configure backup policies for monthly or yearly retention for compliance purposes.

#### **Alerts and Notifications**:
- Set up alerts for backup job failures using **Azure Monitor**.

#### **Cost Optimization**:
- Use the **Azure Pricing Calculator** to estimate costs and optimize the backup schedule.

---

### **5. Troubleshooting**

| **Issue**                                   | **Solution**                                                      |
|---------------------------------------------|--------------------------------------------------------------------|
| Backup fails for VM                         | Ensure the VM is in a supported region and has the Azure Backup agent installed. |
| Restore job fails                           | Verify the storage account and network configuration for the restore. |
| Recovery Services Vault not visible         | Ensure you are in the same subscription and region as the VM.      |
| Unexpected costs                            | Review retention policies and frequency of backups to optimize costs. |

---

### **6. Deliverable**
Users should:
1. Provide a screenshot of the backup job completion status.
2. Share the details of the restored VM (e.g., name, recovery point used).

---

### **7. Learning Outcomes**
Users will:
- Understand how to set up a **Recovery Services Vault** in Azure.
- Learn to configure **backup policies** and trigger backups for Azure Virtual Machines.
- Gain experience in restoring resources from backups in disaster recovery scenarios.

---

This hands-on project provides users with critical skills in **disaster recovery and data protection** using Azure Recovery Services. Let me know if you'd like more advanced features or integrations!