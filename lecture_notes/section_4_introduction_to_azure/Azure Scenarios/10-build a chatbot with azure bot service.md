### **Scenario 10: Build a Chatbot with Azure Bot Service**

This scenario introduces users to creating a chatbot using **Azure Bot Service**. They will develop a simple bot, deploy it on Azure, and test it in a web chat interface or integrate it with Microsoft Teams.

---

### **1. Objective**
Users will:
1. Create an **Azure Bot Service**.
2. Develop a basic chatbot using **Azure Bot Framework SDK** or **Composer**.
3. Test the bot in the Azure Web Chat or integrate it with Microsoft Teams.

---

### **2. Prerequisites**
1. **Azure for Students account** with $100 free credits.
2. **Azure CLI** installed locally (optional).
3. Basic understanding of programming (Python or JavaScript).

---

### **3. Steps**

#### **Step 1: Create an Azure Bot Service**

1. **Log in to Azure Portal**:
   - Go to [Azure Portal](https://portal.azure.com) and sign in.

2. **Navigate to Azure Bot Service**:
   - Search for **Bot Services** in the search bar and click **+ Create**.

3. **Fill in Basic Details**:
   - **Resource Group**: Create or select an existing group (e.g., `chatbot-project`).
   - **Bot Handle**: Enter a unique name (e.g., `user-chatbot`).
   - **Region**: Select a region close to you.
   - **Pricing Tier**: Choose **Free**.
   - **App Type**: Choose **Web App Bot**.
   - **Bot Template**: Select **Echo Bot** (basic bot template).
   - **App Service Plan**: Use the free or basic tier.

4. **Review and Create**:
   - Click **Review + Create**, then **Create**.

---

#### **Step 2: Test the Bot**

1. **Navigate to Web Chat**:
   - Once the bot is deployed, go to the Azure Portal.
   - Open the **Web Chat** blade in the Bot Service menu.

2. **Interact with the Bot**:
   - Type a message (e.g., "Hello").
   - The bot should echo your message back.

---

#### **Step 3: Customize the Bot**

##### **Option A: Using Azure Bot Framework Composer**
1. **Download Bot Framework Composer**:
   - Install from [Bot Framework Composer](https://github.com/microsoft/BotFramework-Composer/releases).

2. **Create a New Bot**:
   - Open Composer and create a bot using the **Echo Bot** template.
   - Add custom dialogs or responses:
     - Example: Add a response to "How are you?"
       - User input: "How are you?"
       - Bot response: "I’m just a bot, but I’m here to help!"

3. **Publish the Bot**:
   - In Composer, click **Publish** to deploy the customized bot to Azure.

##### **Option B: Customize Using Code**
1. **Download the Bot Code**:
   - Navigate to the Bot Service in Azure Portal.
   - Go to **Build** and download the bot source code.

2. **Modify the Code**:
   - Open the bot project in an editor like **Visual Studio Code**.
   - Update the bot logic in the main file (e.g., `app.py` for Python or `index.js` for Node.js).

   **Example (Node.js)**:
   ```javascript
   const { ActivityHandler } = require('botbuilder');

   class EchoBot extends ActivityHandler {
       constructor() {
           super();
           this.onMessage(async (context, next) => {
               const text = context.activity.text;
               if (text.toLowerCase() === "how are you?") {
                   await context.sendActivity("I'm a bot, but I'm doing great!");
               } else {
                   await context.sendActivity(`You said: ${text}`);
               }
               await next();
           });
       }
   }

   module.exports.EchoBot = EchoBot;
   ```

3. **Redeploy the Bot**:
   - Deploy the updated bot back to Azure using **Azure CLI** or the Azure Portal.

---

#### **Step 4: Integrate the Bot with a Channel**

1. **Navigate to Channels**:
   - In the Bot Service, go to **Channels** under **Settings**.

2. **Add a Channel**:
   - Select a channel to integrate with, such as **Microsoft Teams**, **Slack**, or **Direct Line**.
   - Follow the instructions for each channel to configure and publish the bot.

3. **Test the Bot**:
   - Open the selected channel (e.g., Teams).
   - Search for the bot by its name and start a conversation.

---

### **4. Optional Enhancements**

#### **Add Natural Language Understanding (LUIS)**:
1. Integrate the bot with **Azure Language Understanding (LUIS)**.
2. Train LUIS to recognize intents (e.g., "Book a flight") and entities (e.g., "Destination").

#### **Add Azure Cognitive Services**:
- Enhance the bot’s capabilities with **Text Analytics**, **Speech-to-Text**, or **Translator**.

#### **Add Proactive Messaging**:
- Program the bot to send messages proactively (e.g., reminders or alerts).

#### **Create a Multi-Turn Conversation**:
- Add dialogs to handle multi-turn conversations (e.g., booking appointments or answering FAQs).

---

### **5. Troubleshooting**

| **Issue**                                | **Solution**                                                      |
|------------------------------------------|--------------------------------------------------------------------|
| Bot doesn’t respond in Web Chat          | Check the deployment status in the Azure Portal.                  |
| Unable to test in Teams or Slack         | Verify channel configuration and permissions.                     |
| Deployment fails                         | Review logs in the Azure App Service linked to the bot.           |
| Custom logic not working                 | Debug locally using the Bot Framework Emulator.                   |

---

### **6. Deliverable**
Users should:
1. Provide the bot’s **Web Chat URL** or **Teams integration link**.
2. Share screenshots of interactions with the bot.

---

### **7. Learning Outcomes**
Users will:
- Understand how to create and deploy a chatbot using **Azure Bot Service**.
- Customize chatbot behavior with **Composer** or **code**.
- Explore multi-channel integration and enhance bot functionality.

---

This project provides users with practical experience in building and deploying intelligent chatbots. Let me know if you'd like to include more advanced features like AI integration!