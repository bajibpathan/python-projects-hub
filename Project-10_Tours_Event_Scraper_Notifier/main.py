import smtplib
import requests
import selectorlib
import sqlite3
import os
from email.message import EmailMessage
from contextlib import closing


# ---------------- CONFIG ----------------
URL = "https://programmer100.pythonanywhere.com/tours/"
DB_PATH = "data.db"
YAML_PATH = "extract.yaml"

SENDER = os.getenv("EMAIL_SENDER")
PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER = os.getenv("EMAIL_RECEIVER")


# ---------------- DATABASE ----------------
def get_connection():
    """
    Creates and returns a SQLite connection.
    Using a function avoids keeping a global connection open forever.
    """
    return sqlite3.connect(DB_PATH)


# ---------------- SCRAPING ----------------
def scrape(url: str) -> str:
    """
    Scrapes the HTML source from the given URL with headers and timeout.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/39.0.2171.95 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.text


def extract(source: str) -> str:
    """
    Extracts tour data using selectorlib YAML configuration.
    """
    extractor = selectorlib.Extractor.from_yaml_file(YAML_PATH)
    return extractor.extract(source)["tours"]


# ---------------- EMAIL ----------------
def send_email(message: str) -> None:
    """
    Sends an email notification when a new event is detected.
    """
    email_message = EmailMessage()
    email_message["Subject"] = "🎸 New Event Found!"
    email_message["From"] = SENDER
    email_message["To"] = RECEIVER
    email_message.set_content(f"Hey,\n\nA new event was found:\n\n{message}")

    with smtplib.SMTP("smtp.gmail.com", 587) as gmail:
        gmail.ehlo()
        gmail.starttls()
        gmail.login(SENDER, PASSWORD)
        gmail.send_message(email_message)

    print("✅ Email sent successfully.")


# ---------------- DATABASE OPERATIONS ----------------
def parse_event(extracted: str):
    """
    Parses the extracted string into structured fields.
    """
    row = [item.strip() for item in extracted.split(",")]
    return row


def store(extracted: str) -> None:
    """
    Stores a new event into the database.
    """
    row = parse_event(extracted)

    with closing(get_connection()) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO events VALUES (?,?,?)", row)
        connection.commit()


def read(extracted: str):
    """
    Checks if the event already exists in the database.
    """
    band, city, date = parse_event(extracted)

    with closing(get_connection()) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM events WHERE band=? AND city=? AND date=?",
            (band, city, date),
        )
        return cursor.fetchall()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    print("🔎 Scraping website...")

    scraped = scrape(URL)
    extracted = extract(scraped)
    print("📌 Extracted:", extracted)

    if extracted and extracted != "No upcoming tours":
        rows = read(extracted)

        if not rows:
            store(extracted)
            send_email(extracted)
        else:
            print("ℹ️ Event already exists in database.")
