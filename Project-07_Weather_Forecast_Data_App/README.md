# 🌤 Weather Forecast App (Streamlit + Plotly)

This project is a simple and interactive **Weather Forecast Web App** built using **Streamlit**, **Plotly**, and the **OpenWeatherMap API**.  
Users can search for a city and visualize upcoming weather data such as **temperature trends** and **sky conditions**.

---

## 🚀 Features

- Search weather by city name
- Select number of forecast days (1–5)
- Visualize temperature trends with Plotly
- Display sky conditions with icons
- Error handling for invalid cities
- Clean UI using Streamlit

---

## 🛠 Tech Stack

- Python
- Streamlit
- Plotly
- Requests
- Python-dotenv
- OpenWeatherMap API

---

## 📂 Project Structure
```
Weather_Forecast_Data_App/
│
├── main.py
├── backend.py
├── images/
│ ├── clear.png
│ ├── cloud.png
│ ├── rain.png
│ └── snow.png
├── .env
└── requirements.txt
```

---

## ⚙️ Setup Instructions

#### 1️⃣ Clone the Repository

#### 2️⃣ Create Virtual Environment (Optional)
```bash
python -m venv venv
source venv/bin/activate
```

#### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ Create .env File

Inside the project folder:
```bash
WEATHER_API_KEY=your_openweather_api_key
```

Get your API key from:
👉 https://openweathermap.org/api

#### 5️⃣ Run the App
```bash
streamlit run main.py
```

#### 📌 Usage

- Enter a city name.
- Select number of days.
- Choose between Temperature or Sky view.
- Explore your weather forecast visually.

---
### 🙌 Acknowledgements

- OpenWeatherMap API
- Streamlit
- Plotly

---

## 📚 Credits & Acknowledgements

Special thanks to all educators and contributors who share knowledge and make learning accessible. 🙏

---
⭐ If you like this project, give it a star!