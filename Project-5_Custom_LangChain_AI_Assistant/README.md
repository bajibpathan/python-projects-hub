# 🧠 Chat With Einstein (Gemini + LangChain + Gradio)

This project is an interactive AI chatbot that lets users have a conversation with **Albert Einstein's personality**.  
It uses **Google Gemini**, **LangChain**, and **Gradio** to create a smart, reasoning-based conversational experience.

Einstein answers questions with:
- Deep reasoning  
- Personal reflections  
- Scientific explanations  
- Life experiences  

---

## 🚀 Features

- Gemini-powered AI responses  
- Einstein-style personality prompt  
- Memory-aware conversations  
- Web UI using Gradio  
- Clean LangChain pipeline with chaining  
- Supports chat history  
- Streaming-ready architecture  

---

## 🧰 Tech Stack

- Python  
- LangChain  
- Google Gemini API  
- Gradio  
- python-dotenv  

---

## 📦 Installation

1. Clone the repository:
2. Install dependencies:
```bash
pip install -r requirements.txt
```
---

## 🔑 Environment Setup

Create a .env file in the project root:

```bash
GEMINI_API_KEY=your_google_gemini_api_key
```

▶️ Run the App
```bash
python main.py
```

Then open the Gradio link in your browser.

---

## 🧠 How It Works

- User enters a message in Gradio UI
- Chat history is converted into LangChain messages
- Prompt + History are sent to Gemini
- Gemini generates Einstein-style output
- Output is parsed and shown in UI

Pipeline used:

```python
chain = prompt | llm | StrOutputParser()
```

Which represents:
```nginx
Prompt → Gemini → Output Parser
```
---

## 📂 Project Structure
```text
.
├── main.py
├── requirements.txt
├── .env
├── einstein.png
└── README.md
```
---

## 📚 Credits & Acknowledgements

Inspired by:
- LangChain
- Google Gemini
- Gradio
- Open-source AI community

Special thanks to all educators and contributors who share knowledge and make learning accessible. 🙏

---
⭐ If you like this project, give it a star!