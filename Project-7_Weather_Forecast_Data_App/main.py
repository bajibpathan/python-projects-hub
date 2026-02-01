import streamlit as st
import plotly.express as px
from backend import get_data

# ---------------- UI SETUP ----------------
st.title("🌤 Weather Forecast for the Next Days")

place = st.text_input("Place:")
days = st.slider(
    "Forecast Days",
    min_value=1,
    max_value=5,
    help="Select the number of forecasted days"
)

option = st.selectbox("Select data to view", ("Temperature", "Sky"))


# ---------------- MAIN LOGIC ----------------
if place:
    filtered_data = get_data(place, days)

    # Handle incorrect city input
    if "Incorrect City" in filtered_data:
        st.subheader("You have entered an incorrect city. Please try again!")
    else:
        st.subheader(f"{option} for the next {days} days in {place}")

        # -------- TEMPERATURE VIEW --------
        if option == "Temperature":
            temperatures = [
                item.get("main", {}).get("temp", 0) - 273.15
                for item in filtered_data
            ]

            dates = [item.get("dt_txt") for item in filtered_data]

            figure = px.line(
                x=dates,
                y=temperatures,
                labels={"x": "Date", "y": "Temperature (°C)"},
                title="Temperature Trend"
            )

            st.plotly_chart(figure)

        # -------- SKY VIEW --------
        elif option == "Sky":
            images = {
                "Clear": "images/clear.png",
                "Clouds": "images/cloud.png",
                "Rain": "images/rain.png",
                "Snow": "images/snow.png"
            }

            sky_conditions = [
                item.get("weather", [{}])[0].get("main", "Clear")
                for item in filtered_data
            ]

            image_paths = [
                images.get(condition, "images/clear.png")
                for condition in sky_conditions
            ]

            st.image(image_paths, caption=sky_conditions, width=100)
