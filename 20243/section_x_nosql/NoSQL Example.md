Let’s walk through a practical example of using MongoDB Community Server edition to set up a database for a small project, like a "task manager" app.

### Step 1: Install MongoDB Community Server
1. Download MongoDB Community Server from [MongoDB’s website](https://www.mongodb.com/try/download/community).
2. Follow the installation instructions for your operating system.

### Step 2: Start MongoDB
1. After installation, start the MongoDB service:
   - On Windows, run `mongod` from the command line.
   - On macOS or Linux, you might start MongoDB with a command like `brew services start mongodb-community` (if installed via Homebrew) or by running `mongod` directly.

### Step 3: Access MongoDB through the MongoDB Shell
1. In a new terminal window, type `mongo` to open the MongoDB shell.
2. You should now be connected to your local MongoDB server.

### Step 4: Create a Database and Collection
Let's create a new database called "taskManager" and a collection (similar to a table in SQL) called "tasks."

```javascript
use taskManager
db.createCollection("tasks")
```

### Step 5: Insert Data into the Collection
Now, we’ll add some example tasks to the collection. Each document (equivalent to a row in SQL) is represented in JSON-like format.

```javascript
db.tasks.insertMany([
  { title: "Buy groceries", dueDate: new Date("2023-11-10"), status: "pending" },
  { title: "Complete MongoDB tutorial", dueDate: new Date("2023-11-15"), status: "in-progress" },
  { title: "Schedule meeting with client", dueDate: new Date("2023-11-20"), status: "completed" }
])
```

### Step 6: Query Data
Retrieve all pending tasks:

```javascript
db.tasks.find({ status: "pending" })
```

Or find tasks due before a specific date:

```javascript
db.tasks.find({ dueDate: { $lt: new Date("2023-11-15") } })
```

### Step 7: Update Data
Update a task status to "completed":

```javascript
db.tasks.updateOne(
  { title: "Buy groceries" },
  { $set: { status: "completed" } }
)
```

### Step 8: Delete Data
Remove tasks with a completed status:

```javascript
db.tasks.deleteMany({ status: "completed" })
```

### Step 9: Close MongoDB
To stop the MongoDB service:
- On Windows, you can close the command prompt running `mongod`.
- On macOS or Linux, use the appropriate service stop command.

This example demonstrates how to use MongoDB Community Server to set up a small, local database for a task management application. You can further expand this with additional collections or integrate it with application code (like Node.js) for more dynamic interaction.
