# 📝 Django Job Application Form

A production-ready Django web application that allows users to submit a job application form. The application stores user data in a database and optionally sends confirmation emails upon submission.

This project demonstrates:
- Django Models & ORM
- Form handling & validation
- Email integration
- SQLite database usage
- Environment variable configuration

---

## 🚀 Features

- ✅ Post job listings
- ✅ Submit job applications
- ✅ Track application status
- ✅ User authentication and profiles
- ✅ Admin dashboard for management

---

## 🛠 Tech Stack

- Backend: Django
- Database: SQLite (default)
- Frontend: HTML, Bootstrap 5
- Email Service: SMTP (Gmail example)
- Environment Management: python-dotenv

---

## Requirements

- Python 3.8+
- Django 3.2+
- SQLite (default database)

---

## ⚙️ Installation & Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Crate a .env file in root directory and update the email user & password 
```env
SECRET_KEY=your_secret_key
DEBUG=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

```
5. Apply migrations: 
```bash
python manage.py makemigrations
python manage.py migrate
```
6. Start the server: `python manage.py runserver`

## Usage

- Navigate to `http://localhost:8000`
- Create an account or log in
- Browse job postings and apply
- Check application status in your dashboard

## Project Structure

```
django-job-form/
│
├── manage.py
├── requirements.txt
├── README.md
├── .env
│
├── project_name/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── app_name/
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    └── templates/
        └── index.html
```

---

## 📚 Credits & Acknowledgements

Special thanks to all educators and contributors who share knowledge and make learning accessible. 🙏

---

⭐ If you like this project, give it a star!
