# 🚀 Flask Job Application Web App

## 📌 Overview

A professional web application built with Flask that:

- Collects job application data
- Stores information in SQLite database
- Sends confirmation email
- Displays success/error notifications

---

## 🛠 Tech Stack

- Python 3.9+
- Flask
- SQLAlchemy
- Flask-Mail
- SQLite
- Bootstrap 5

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/flask-job-app.git
cd flask-job-app
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables (Important)

Create a .env file or export:

```bash
export SECRET_KEY=your_secret_key
export MAIL_USERNAME=your_email@gmail.com
export MAIL_PASSWORD=your_app_password
```

⚠️ Never commit credentials to GitHub.

---

## ▶️ Run Application

```bash
python app.py
```

Visit:

```arduino
http://localhost:5001
```

---

## 📂 Project Structure

```text
flask-job-app/
│
├── app.py
├── templates/
│   └── index.html
├── data.db
├── requirements.txt
└── README.md
```

---

## 🔐 Security Best Practices

- Environment variables used for secrets
- Unique email constraint
- Input validation
- Exception handling
- SQLAlchemy ORM (prevents SQL injection)

---

## 📦 requirements.txt

```python
Flask==3.0.0
Flask-SQLAlchemy==3.1.1
Flask-Mail==0.9.1
```

## 📚 Credits & Acknowledgements

Special thanks to all educators and contributors who share knowledge and make learning accessible. 🙏

---

⭐ If you like this project, give it a star!
