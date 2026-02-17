# ✅ AI Todoist Agent with LangChain & Gemini

An interactive **AI-powered Todoist assistant** built with **Python, LangChain, and Google Gemini**.

This agent allows you to manage your Todoist tasks using natural language — you can add tasks, view tasks, and interact conversationally through the terminal.

---

## 🚀 Features

- Add Todoist tasks using natural language  
- Show all existing tasks  
- Conversational memory support  
- Google Gemini LLM integration  
- Tool-based agent execution with LangChain  

---

## 🛠 Tech Stack

- Python  
- LangChain  
- Google Gemini  
- Todoist API  
- python-dotenv  

---

## 📂 Project Structure

```text
ai-todoist-agent/
│
├── todoist_agent.py
├── .env
└── README.md
```

---
## ▶️ Setup & Run

1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

2️⃣ Create .env file
```bash
TODOIST_API_KEY=your_todoist_key
GEMINI_API_KEY=your_gemini_key
```

3️⃣ Run the agent
```bash
python todoist_agent.py
```
---

## ✨ Example Usage

You: Add a task to study Python tonight
AI: ✅ Task added successfully.

You: Show me the tasks
AI:
• Study Python tonight
• Prepare interview notes

---

## 🧠 How It Works
- Loads secrets securely using dotenv
- Creates Todoist tools (add_task, show_tasks)
- Configures Gemini as the LLM
- Uses LangChain agent with tools
- Maintains conversation history
- Executes user intent automatically

---
## 📚 Credits & Thanks

This project is created for learning purposes using inspiration from LangChain, Google Gemini, and the open-source community.

🙏 Thanks to all educators and contributors.

---
⭐ If you like this project, give it a star!