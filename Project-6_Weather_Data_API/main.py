from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

# -------------------- LOAD STATIONS --------------------
# Load stations once at startup instead of every request
stations = pd.read_csv("data/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]
stations.columns = stations.columns.str.strip()

# -------------------- HELPERS --------------------
def load_station_data(station_id):
    """
    Load temperature data for a given station.
    Cleans column names and parses DATE column.
    """
    filename = f"data/TG_STAID{str(station_id).zfill(6)}.txt"

    if not os.path.exists(filename):
        return None

    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    df.columns = df.columns.str.strip()
    return df


# -------------------- ROUTES --------------------
@app.route("/")
def home():
    """Render homepage with list of stations."""
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/stations")
def stations_all():
    """Return all teh stations information."""
    return jsonify(stations.to_dict(orient="records"))

@app.route("/api/v1/stations/<station_id>/temperatures/<date>")
def station_date(station_id, date):
    """Return temperature for a station on a specific date."""
    df = load_station_data(station_id)
    temperature = df.loc[df["DATE"] == date]["TG"].squeeze() / 10
    response = { "station": station_id, "date": date, "temperature": temperature }
    return jsonify(response)


@app.route("/api/v1/stations/<station_id>/temperatures")
def station_all(station_id):
    """Return all data for a station."""
    df = load_station_data(station_id)
    result = df.to_dict(orient="records")
    return jsonify(result)


@app.route("/api/v1/stations/<station_id>/temperatures/year/<year>")
def yearly(station_id, year):
    """Return yearly data for a station."""

    df = load_station_data(station_id)
    df.columns = df.columns.str.strip()
    df["DATE"] = df["DATE"].astype(str)
    result = df[df["DATE"].str.startswith(str(year))].to_dict(orient="records")
    return jsonify(result)

# -------------------- RUN --------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)