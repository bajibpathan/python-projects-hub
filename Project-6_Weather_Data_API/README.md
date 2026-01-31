# 🌤 Weather Data API (Flask + Pandas)

This project is a RESTful API built with **Flask** and **Pandas** that provides historical temperature data for weather stations.

It reads weather data from text files and exposes endpoints to query:

- All stations
- All temperatures for a station
- Temperature for a specific date
- Yearly temperature data

---

## 🚀 Features

- REST-style API design
- JSON responses
- Error handling for missing stations
- Fast CSV loading with helpers
- Clean route naming
- Easy to extend

---

## 🛠 Tech Stack

- Python
- Flask
- Pandas
- HTML (Jinja2 Templates)

---

## 📦 Installation

1️⃣ Clone the repo

```bash
git clone <your-repo-url>
cd your-repo-name
```

2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
---

## 📁 Data Dependency (Important)

This project depends on external weather data files.

Before running the app, make sure you:

- Create a folder named:
```
data/
```

- Place the following files inside it:
```
stations.txt
TG_STAIDxxxxxx.txt   (multiple station files)
```
---

## ▶ Run the App
```bash
python main.py
```

Then open:
```bash
http://127.0.0.1:5000
```
---

## 🔗 API Endpoints

|Method	|Endpoint	|Description|
|--|--|--|
|GET|	/api/v1/stations|	List all stations|
|GET|	/api/v1/stations/<station_id>/|temperatures|	All data for a station
|GET|	/api/v1/stations/<station_id>/|temperatures/<date>|	One day temperature
|GET|	/api/v1/stations/<station_id>/|temperatures/year/<year>|	Yearly temperatures|

---

## ✅ Examples
```bash
/api/v1/stations
/api/v1/stations/10/temperatures
/api/v1/stations/10/temperatures/1988-10-25
/api/v1/stations/10/temperatures/year/1988
```
---


## 📂 Project Structure
```
project/
│
├── main.py
├── requirements.txt
├── data/
│   ├── stations.txt
│   ├── TG_STAID000010.txt
│   ├── TG_STAID000011.txt
│   └── ..
├── templates/
│   └── home.html
│
└── README.md
```

---

## 📚 Credits & Acknowledgements

Special thanks to all educators and contributors who share knowledge and make learning accessible. 🙏

---
⭐ If you like this project, give it a star!