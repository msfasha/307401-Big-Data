### **Scenario 4: Build a Serverless Function with Azure Functions**

This scenario introduces users to **Azure Functions**, a serverless compute service for running lightweight code in response to events. Users will create a simple HTTP-triggered Azure Function and test it using a web browser or an API tool like Postman.

---

### **1. Objective**
Users will:
1. Create an **Azure Function App**.
2. Write and deploy a serverless HTTP-triggered function.
3. Test the function via a web browser or API client.

---

### **2. Prerequisites**
1. **Azure for Students account** with $100 free credits.
2. Basic knowledge of programming in **Python** or **JavaScript**.
3. An API testing tool like **Postman** (optional).

---

### **3. Steps**

#### **Step 1: Create a Function App**

1. **Log in to Azure Portal**:
   - Go to [Azure Portal](https://portal.azure.com) and sign in.

2. **Navigate to Function App**:
   - Search for **Function App** in the search bar and click **+ Create**.

3. **Fill in Basic Details**:
   - **Subscription**: Select your subscription.
   - **Resource Group**: Create or select a resource group (e.g., `serverless-functions`).
   - **Function App Name**: Enter a unique name (e.g., `user-function-app`).
   - **Region**: Choose a region close to your location.
   - **Runtime Stack**: Select a language, e.g., **Python** or **JavaScript**.
   - **Version**: Choose the latest version.
   - **Operating System**: Choose **Windows** or **Linux**.
   - **Plan Type**: Select **Consumption (Serverless)** for a pay-per-execution model.

4. **Review and Create**:
   - Click **Review + Create**, then **Create** to deploy the Function App.

---

#### **Step 2: Create an HTTP-Triggered Function**

1. **Go to the Function App**:
   - After deployment, navigate to the **Function App** in the Azure Portal.

2. **Create a New Function**:
   - Click **Functions** > **+ Add**.
   - Select **HTTP Trigger** as the template.
   - Enter a name for the function (e.g., `HttpTriggerExample`).
   - Set **Authorization Level** to **Anonymous** (to allow public access).
   - Click **Create**.

3. **Write the Function Code**:
   - Navigate to the **Code + Test** tab in the function.
   - Replace the default code with the following example:

   **Python Example**:
   ```python
   import logging

   import azure.functions as func

   def main(req: func.HttpRequest) -> func.HttpResponse:
       logging.info('HTTP trigger function processed a request.')

       name = req.params.get('name')
       if not name:
           try:
               req_body = req.get_json()
           except ValueError:
               pass
           else:
               name = req_body.get('name')

       if name:
           return func.HttpResponse(f"Hello, {name}!")
       else:
           return func.HttpResponse(
               "Please pass a name in the query string or in the request body.",
               status_code=400
           )
   ```

   **JavaScript Example**:
   ```javascript
   module.exports = async function (context, req) {
       context.log('HTTP trigger function processed a request.');

       const name = req.query.name || (req.body && req.body.name);
       if (name) {
           context.res = {
               // status: 200, /* Defaults to 200 */
               body: `Hello, ${name}!`
           };
       } else {
           context.res = {
               status: 400,
               body: "Please pass a name in the query string or in the request body."
           };
       }
   };
   ```

4. **Save and Test the Function**.

---

#### **Step 3: Test the Function**

1. **Get the Function URL**:
   - Go to the **Function** in the Azure Portal.
   - Click **Get Function URL** and copy the URL.

2. **Test Using a Web Browser**:
   - Append `?name=YourName` to the URL.
   - Example: `https://user-function-app.azurewebsites.net/api/HttpTriggerExample?name=John`.
   - The browser should display: `Hello, John!`

3. **Test Using Postman (Optional)**:
   - Open Postman or any API testing tool.
   - Send a **POST request** to the Function URL with the following JSON body:
     ```json
     {
         "name": "John"
     }
     ```
   - Verify the response: `Hello, John!`

---

#### **Step 4: Monitor Function Performance**

1. **View Logs**:
   - In the Azure Portal, go to the Function App > **Monitor**.
   - Check logs to see the function execution details.

2. **View Metrics**:
   - Monitor invocation count, execution time, and errors.

---

### **4. Optional Enhancements**

#### **Add Input Validation**:
- Modify the function to validate additional input fields, like age or email.

#### **Trigger Based on Storage Events**:
- Create a function triggered when a file is uploaded to **Blob Storage**.

#### **Integrate with a Database**:
- Save the input data to **Azure Cosmos DB** or **Azure SQL Database**.

#### **Deploy from Code**:
- Use **Azure DevOps** or **GitHub Actions** to deploy the function from a source code repository.

---

### **5. Troubleshooting**

| **Issue**                                 | **Solution**                                                         |
|-------------------------------------------|----------------------------------------------------------------------|
| Cannot access the function                | Ensure **Authorization Level** is set to **Anonymous**.             |
| 500 Internal Server Error                 | Check the logs in the **Monitor** tab for debugging information.     |
| Response is slow                          | Verify the **App Service Plan** (Consumption Plan may introduce cold starts). |
| Missing runtime or dependencies           | Ensure the correct **Runtime Stack** and libraries are installed.    |

---

### **6. Deliverable**
Users should:
1. Share the **Function URL**.
2. Provide screenshots of the response in a browser or Postman.

---

### **7. Learning Outcomes**
Users will:
- Understand the basics of **serverless computing**.
- Learn to create and deploy **HTTP-triggered functions**.
- Gain experience testing APIs using tools like Postman.
- Explore how Azure Functions integrate with other Azure services.

---

This project gives users a solid introduction to **serverless architectures** with Azure Functions. Let me know if you’d like to add more advanced scenarios!