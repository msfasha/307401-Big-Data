### **Scenario 5: Deploy a Web App Using Azure App Service**

In this scenario, users will learn how to deploy a simple web application using **Azure App Service**, a platform-as-a-service (PaaS) offering for hosting web apps without managing the underlying infrastructure.

---

### **1. Objective**
Users will:
1. Create an **Azure App Service**.
2. Deploy a sample web app to the service using **Azure CLI** or **GitHub**.
3. Access the live application via a public URL.

---

### **2. Prerequisites**
1. **Azure for Students account** with $100 free credits.
2. A simple web app, such as a **Python Flask**, **Node.js**, or **HTML/CSS** app.
3. Optional tools:
   - **Azure CLI** installed locally.
   - A **GitHub account** (if deploying via GitHub).

---

### **3. Steps**

#### **Step 1: Create an Azure App Service**
1. **Log in to Azure Portal**:
   - Go to [Azure Portal](https://portal.azure.com) and sign in.

2. **Navigate to App Services**:
   - Search for **App Services** in the search bar and click **+ Create**.

3. **Fill in Basic Details**:
   - **Subscription**: Select your subscription.
   - **Resource Group**: Create or select a resource group (e.g., `web-app-project`).
   - **Name**: Enter a unique name for the app (e.g., `user-web-app`).
   - **Publish**: Select **Code** (if deploying a web app via code) or **Docker** (for containerized apps).
   - **Runtime Stack**: Choose the language for your app (e.g., **Python**, **Node.js**, or **PHP**).
   - **Region**: Choose a region close to your location.
   - **App Service Plan**: Select **Free** or **Basic** to keep costs low.

4. **Review and Create**:
   - Click **Review + Create**, then **Create** to deploy the App Service.

---

#### **Step 2: Deploy the Web App**

##### **Option 1: Use Azure CLI**
1. **Prepare Your Code**:
   - Ensure you have a local folder containing your web app files (e.g., Flask, Node.js, or HTML).
   - Example: A simple Flask app (`app.py`):
     ```python
     from flask import Flask
     app = Flask(__name__)

     @app.route('/')
     def home():
         return 'Hello from Azure App Service!'
     ```

2. **Install Azure CLI**:
   - If not already installed, follow [Azure CLI installation instructions](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).

3. **Deploy the App**:
   - Open a terminal, navigate to the app directory, and run:
     ```bash
     az login
     az webapp up --name <app-service-name> --resource-group <resource-group-name> --runtime "PYTHON:3.8"
     ```
   - Replace `<app-service-name>` and `<resource-group-name>` with the names you set in Step 1.

4. **Verify Deployment**:
   - Once deployed, Azure will provide a URL (e.g., `https://user-web-app.azurewebsites.net`).
   - Open the URL in a browser to verify the app is running.

---

##### **Option 2: Deploy from GitHub**
1. **Push Code to GitHub**:
   - Create a new GitHub repository and push your web app code to it.

2. **Connect GitHub to Azure**:
   - In the Azure Portal, navigate to your App Service.
   - Click **Deployment Center** under **Deployment**.
   - Select **GitHub** as the source and authenticate your GitHub account.
   - Choose your repository and branch.

3. **Deploy the App**:
   - Click **Save** to trigger the deployment.
   - Azure will automatically build and deploy the app using your selected runtime stack.

4. **Verify Deployment**:
   - Open the public URL of the app (e.g., `https://user-web-app.azurewebsites.net`).

---

#### **Step 3: Access and Test the App**
1. Open the **App Service URL** (provided by Azure, e.g., `https://user-web-app.azurewebsites.net`).
2. Ensure the app is functioning as expected.

---

### **4. Optional Enhancements**

#### **Custom Domain Name**:
- Assign a custom domain to your App Service and configure it in the **Custom Domains** section.

#### **HTTPS and Security**:
- Enable HTTPS for secure communication by going to **TLS/SSL Settings** in the Azure Portal.

#### **Environment Variables**:
- Add environment variables (e.g., database credentials) in the **Configuration** section.

#### **CI/CD with GitHub Actions**:
- Set up GitHub Actions to automate deployments whenever code is pushed to the repository.

---

### **5. Troubleshooting**

| **Issue**                                | **Solution**                                                      |
|------------------------------------------|--------------------------------------------------------------------|
| App fails to start                       | Verify the runtime stack matches your app's requirements.          |
| URL not accessible                       | Check the **App Service Plan** and ensure it's running.            |
| Deployment errors                        | Check the **Deployment Center logs** for detailed error messages. |
| Changes to code don’t reflect in app     | Redeploy the app or ensure GitHub integration is properly configured. |

---

### **6. Deliverable**
Users should:
1. Share the **public URL** of the deployed web app.
2. Provide screenshots of the app running in a browser.

---

### **7. Learning Outcomes**
Users will:
- Understand the basics of **Azure App Service** for hosting web applications.
- Deploy web apps using **Azure CLI** or **GitHub integration**.
- Gain experience with serverless, platform-as-a-service (PaaS) solutions.
- Explore the benefits of automated deployments.

---

This scenario is simple and practical, introducing users to modern application hosting using **Azure App Service**. Let me know if you need further refinements or advanced features!