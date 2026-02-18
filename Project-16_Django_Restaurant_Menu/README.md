# 🍽️ Django Restaurant Menu

A Django-based web application for managing and displaying restaurant menus.

--- 
## 🚀 Features

- Browse restaurant menu items
- Categorize menu items (appetizers, mains, desserts, etc.)
- Admin interface for menu management
- Responsive design

---

## 🏗️ Tech Stack
- Backend: Django
- Language: Python
- Database: SQLite (default)
- Frontend: HTML, CSS (Django Templates)
---

## Requirements

- Python 3.8+
- Django 3.2+
- SQLite (default)

---

## ⚙️ Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install django
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

--- 

## Usage

Start the development server:

```bash
python manage.py runserver
```

Access the application at `http://localhost:8000`

Admin panel: `http://localhost:8000/admin`

## 📂 Project Structure

```
Project-16_Django_Restaurant_Menu/
├── manage.py
├── menu/
│   ├── models.py
│   ├── views.py
│   └── urls.py
└── templates/
```

## 📚 Credits & Acknowledgements

Special thanks to all educators and contributors who share knowledge and make learning accessible. 🙏

---

⭐ If you like this project, give it a star!
