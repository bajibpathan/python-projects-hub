# 🎫 Tour Event Scraper & Notifier

A Python automation project that scrapes upcoming tour events from a website, stores them in a SQLite database, and sends email alerts when a new event is detected.

This project demonstrates web scraping, data extraction, persistence, and automated notification workflows.

---

## 🚀 Features

- Web scraping using `requests`
- Data extraction using `selectorlib`
- SQLite database storage
- Duplicate event detection
- Email notifications via SMTP
- Secure credential handling
- Clean, modular Python design

---

## 🛠 Tech Stack

- Python 3.9+
- Requests
- SelectorLib
- SQLite3
- SMTP / EmailMessage

---

## 📂 Project Structure
```text
project-root/
│
├── main.py
├── extract.yaml
├── data.db
├── requirements.txt
└── README.md
```


---

## ⚙️ Installation

Clone the repository and install dependencies:

```bash
git clone <repo>
cd <to-the-project-foler>
pip install -r requirements.txt
```
---

## 🔐 Environment Variables

Set your email credentials:

### macOS / Linux
```bash
export EMAIL_SENDER="your_email@gmail.com"
export EMAIL_PASSWORD="your_app_password"
export EMAIL_RECEIVER="receiver@gmail.com"
```

### Windows (PowerShell)
```powershell
setx EMAIL_SENDER "your_email@gmail.com"
setx EMAIL_PASSWORD "your_app_password"
setx EMAIL_RECEIVER "receiver@gmail.com"
```
---

## ▶️ Run the App
```bash
python main.py
```

The script will scrape the site, check for new events, store them, and send an email if a new one is found.

---

## 🧠 How It Works

1. Scrapes the website URL.
2. Extracts tour data using YAML rules.
3. Checks SQLite database for duplicates.
4. Stores unseen events.
5. Sends email notifications.

---

## 📦 Dependencies

All dependencies are listed in requirements.txt:
- ``requests`` – HTTP requests
- ``selectorlib`` – Structured scraping

SQLite and SMTP are part of Python’s standard library.

---


## 📚 Credits & Acknowledgements

Special thanks to all educators and contributors who share knowledge and make learning accessible. 🙏

---
⭐ If you like this project, give it a star!