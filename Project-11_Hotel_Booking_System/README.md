# 🏨 Hotel Booking System (CSV-Based)

A Python object-oriented hotel booking system that uses CSV files as a lightweight database. The application allows users to reserve hotels, validate credit cards, authenticate payments, and optionally book SPA packages.

This project demonstrates OOP design, pandas data handling, and simple transaction workflows.

---

## 🚀 Features

- Hotel availability checking
- Booking persistence using CSV files
- Credit card validation
- Secure card authentication
- Reservation ticket generation
- Optional SPA booking
- Object-Oriented design using Python

---

## 🛠 Tech Stack

- Python 3.9+
- Pandas
- CSV Files (Data Persistence)
- OOP Design

---

## 📂 Project Structure
```text
project-root/
│
├── hotels.csv
├── cards.csv
├── card_security.csv
├── main.py
├── requirements.txt
└── README.md
```
---

## 📄 CSV File Dependencies

This project depends on the following CSV files:

### `hotels.csv`

Required columns:

```text
id,name,available
Example:

1,Grand Hotel,yes
2,Sea Resort,no
```

```cards.csv```

Required columns:
```
number,expiration,holder,cvc
```
Example:
```csv
1234567890123456,12/26,JOHN SMITH,123
```
```card_security.csv```
Required columns:
```text
number,password
```

Example:
```csv
1234567890123456,mypass
```
---

## ⚙️ Installation
```bash
git clone https://github.com/your-username/hotel-booking-system.git
cd hotel-booking-system
pip install -r requirements.txt
```
---

## 📦 Requirements
Create requirements.txt:
```
pandas==3.0.0
```
---

## ▶️ Run the Application
```bash
python main.py
```

Follow the prompts to book a hotel and optionally reserve a SPA package.

---

## 🧠 How It Works
1. Loads hotel and card data from CSV files.
2. Checks hotel availability.
3. Validates credit card details.
4. Authenticates user password.
5. Updates booking state in CSV.
6. Generates reservation tickets.

---

## 📚 Credits & Acknowledgements

Special thanks to all educators and contributors who share knowledge and make learning accessible. 🙏

---
⭐ If you like this project, give it a star!