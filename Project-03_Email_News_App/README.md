# 📰 Python News Email Automation

A simple **Python automation project** that fetches the latest news articles from **NewsAPI** and sends them via email using **SMTP (Gmail)**.

This project demonstrates API consumption, data processing, and email automation with Python.

---

## 🚀 Features

- Fetch latest news from NewsAPI  
- Filter and format articles  
- Build email content dynamically  
- Send email using Gmail SMTP  
- Automated daily news updates  

---

## 🛠 Tech Stack

- Python  
- Requests  
- SMTP / SSL  
- NewsAPI  

---

## 📂 Project Structure

```text
news-email-automation/
│
├── main.py
├── sender_email.py
├── README.md

```
---

## ▶️ How to Run

1. Install dependencies:

```bash
pip install requests
```

2. Get your API key from:

```bash
https://newsapi.org
```

3. Update credentials in code:

```bash
API_KEY = "YOUR_API_KEY"
USERNAME = "YOUR_EMAIL"
PASSWORD = "YOUR_APP_PASSWORD"
RECEIVER_EMAIL = "RECEIVER_EMAIL"
```

4. Run the script:
```bash
python main.py
```

---

## ✨ How It Works

- Calls NewsAPI with query parameters.
- Extracts top articles.
- Formats the news into an email body.
- Sends the email securely using SMTP SSL.

---

## 📚 Credits & Thanks

This project is built for learning purposes using inspiration from Python documentation and the developer community.

🙏 Thanks to all educators and open-source contributors.

---
⭐ If you like this project, give it a star!