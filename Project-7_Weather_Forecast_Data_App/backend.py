from dotenv import load_dotenv
import requests
import os

# Load environment variables
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
HOURS_PER_DAY = 8


def get_data(place: str, forecast_days: int):
    """
    Fetch weather forecast data from OpenWeatherMap API.

    Args:
        place (str): City name.
        forecast_days (int): Number of forecast days.

    Returns:
        list | str: Filtered weather data or error message.
    """

    url = f"{BASE_URL}?q={place}&appid={WEATHER_API_KEY}"

    try:
        response = requests.get(url, timeout=10)

        data = response.json()
        filtered_data = data["list"]

        # Limit results based on number of days
        nr_values = HOURS_PER_DAY * forecast_days
        return filtered_data[:nr_values]

    except Exception:
        return "Incorrect City"
