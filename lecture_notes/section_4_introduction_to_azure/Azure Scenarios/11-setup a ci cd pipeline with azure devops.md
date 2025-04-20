### **Scenario 11: Set Up a CI/CD Pipeline with Azure DevOps**

This scenario introduces users to creating a **Continuous Integration and Continuous Deployment (CI/CD)** pipeline using **Azure DevOps**. The pipeline will automate the build, testing, and deployment of an application to Azure.

---

### **1. Objective**
Users will:
1. Create a **DevOps Project** in Azure DevOps.
2. Set up a **Git repository** for the application.
3. Configure a **CI/CD pipeline** to build and deploy the application to Azure.

---

### **2. Prerequisites**
1. **Azure for Students account** with $100 free credits.
2. Access to **Azure DevOps Services**: [Azure DevOps](https://dev.azure.com).
3. A simple application:
   - Example: A Python Flask app or Node.js app.
   - Alternatively, clone a sample app: [Azure Sample Repos](https://github.com/Azure-Samples).

---

### **3. Steps**

#### **Step 1: Set Up Azure DevOps**

1. **Log in to Azure DevOps**:
   - Go to [Azure DevOps](https://dev.azure.com) and sign in with your Microsoft account.

2. **Create a New Project**:
   - Click **+ New Project**.
   - Provide a name (e.g., `CI-CD-Project`) and select visibility as **Private**.
   - Click **Create**.

---

#### **Step 2: Create a Git Repository**

1. **Navigate to Repos**:
   - In your Azure DevOps project, go to **Repos** > **Files**.

2. **Initialize a Repository**:
   - Click **Initialize** to create an empty Git repository.

3. **Clone the Repository**:
   - Copy the repository URL.
   - On your local machine, clone the repository:
     ```bash
     git clone <repository-url>
     ```

4. **Add Your Application**:
   - Copy your application files (e.g., Python Flask app) into the repository folder.

5. **Commit and Push**:
   - Commit and push your changes:
     ```bash
     git add .
     git commit -m "Initial commit"
     git push origin main
     ```

---

#### **Step 3: Configure a CI/CD Pipeline**

1. **Navigate to Pipelines**:
   - In Azure DevOps, go to **Pipelines** > **Create Pipeline**.

2. **Select Repository**:
   - Choose **Azure Repos Git** and select the repository you created.

3. **Define the Pipeline**:
   - Use the **Starter Pipeline** or select a template based on your application stack (e.g., Python, Node.js).

   Example **Python Flask Pipeline (YAML)**:
   ```yaml
   trigger:
     - main

   pool:
     vmImage: 'ubuntu-latest'

   steps:
   - task: UsePythonVersion@1
     inputs:
       versionSpec: '3.x'
       addToPath: true

   - script: |
       python -m venv venv
       source venv/bin/activate
       pip install -r requirements.txt
     displayName: 'Install Dependencies'

   - script: |
       python -m unittest discover tests
     displayName: 'Run Tests'

   - task: PublishBuildArtifacts@1
     inputs:
       pathToPublish: '$(System.DefaultWorkingDirectory)'
       artifactName: 'drop'
   ```

4. **Save and Run**:
   - Save the pipeline and trigger a manual run.
   - Verify the pipeline executes successfully (build, test, and publish artifacts).

---

#### **Step 4: Deploy to Azure**

1. **Set Up Deployment Environment**:
   - Create a deployment target in Azure, such as:
     - **Azure App Service**: Use the free tier.
     - **Azure Kubernetes Service (AKS)**: For containerized apps.
     - **Azure Virtual Machine (VM)**: For custom deployment.

2. **Add a Release Pipeline**:
   - In Azure DevOps, go to **Pipelines** > **Releases** > **New Pipeline**.
   - Add an **artifact**:
     - Select the build artifact from the CI pipeline.
   - Add a **Stage**:
     - Select the deployment target (e.g., Azure App Service).

3. **Deploy the Application**:
   - Configure the deployment task:
     - For App Service: Use the **Azure App Service Deploy** task.
     - For VMs: Use the **SSH** or **Custom Script** task.
   - Trigger a release to deploy the application.

4. **Verify Deployment**:
   - Access the deployed application via its public URL (e.g., `https://<app-name>.azurewebsites.net`).

---

### **4. Optional Enhancements**

#### **Add Automated Testing**:
- Include test scripts in the pipeline to run unit or integration tests before deployment.

#### **Multi-Environment Deployment**:
- Set up **staging** and **production** environments and deploy to staging before promoting to production.

#### **Monitor Pipelines**:
- Enable Azure Application Insights to monitor application performance and errors.

#### **Trigger Deployments Automatically**:
- Configure **Continuous Deployment Triggers** to deploy automatically when changes are pushed.

---

### **5. Troubleshooting**

| **Issue**                               | **Solution**                                                      |
|-----------------------------------------|--------------------------------------------------------------------|
| Pipeline fails at the build step        | Verify the YAML configuration and build dependencies.             |
| Deployment to Azure fails               | Ensure the deployment target exists and is properly configured.    |
| Application doesn’t start               | Check the logs in Azure (e.g., App Service logs).                  |
| Permission errors in Azure DevOps       | Ensure the service principal has the required permissions in Azure. |

---

### **6. Deliverable**
Users should:
1. Share the **pipeline run logs** showing successful execution.
2. Provide the **URL of the deployed application**.

---

### **7. Learning Outcomes**
Users will:
- Understand how to automate build and deployment processes using **Azure DevOps**.
- Learn to create and configure **CI/CD pipelines**.
- Gain experience deploying applications to Azure.

---

This project equips users with essential skills in modern software development workflows, including CI/CD and cloud deployments. Let me know if you'd like more details or advanced features!