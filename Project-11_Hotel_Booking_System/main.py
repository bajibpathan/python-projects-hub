import pandas as pd
from pathlib import Path


# ---------------- CONFIG ----------------
DATA_DIR = Path(".")
HOTELS_FILE = DATA_DIR / "hotels.csv"
CARDS_FILE = DATA_DIR / "cards.csv"
SECURITY_FILE = DATA_DIR / "card_security.csv"


# ---------------- DATA LOADING ----------------
# Load once at startup to avoid repeated disk I/O
df_hotels = pd.read_csv(HOTELS_FILE, dtype={"id": str})
df_cards = pd.read_csv(CARDS_FILE, dtype=str).to_dict(orient="records")
df_cards_security = pd.read_csv(SECURITY_FILE, dtype=str)


# ---------------- MODELS ----------------
class Hotel:
    """
    Represents a hotel and provides booking operations.
    """

    def __init__(self, hotel_id: str):
        self.hotel_id = hotel_id
        self.name = df_hotels.loc[df_hotels["id"] == self.hotel_id, "name"].squeeze()

    def available(self) -> bool:
        """
        Check if the hotel is available.
        """
        availability = df_hotels.loc[df_hotels["id"] == self.hotel_id, "available"].squeeze()
        return availability == "yes"

    def book(self) -> None:
        """
        Book a hotel by marking it unavailable and persisting to CSV.
        """
        df_hotels.loc[df_hotels["id"] == self.hotel_id, "available"] = "no"
        df_hotels.to_csv(HOTELS_FILE, index=False)


class SpaHotel(Hotel):
    """
    Extension of Hotel that supports SPA packages.
    """

    def book_spa_package(self):
        # Placeholder for SPA booking logic
        print(f"🧖 SPA package booked for {self.name}.")


class ReservationTicket:
    """
    Generates a hotel reservation ticket.
    """

    def __init__(self, customer_name: str, hotel_obj: Hotel):
        self.customer_name = customer_name
        self.hotel = hotel_obj

    def generate(self) -> str:
        return f"""
Thank you for your reservation!

Booking Details:
Customer Name: {self.customer_name}
Hotel Name: {self.hotel.name}
"""


class CreditCard:
    """
    Handles credit card validation.
    """

    def __init__(self, number: str):
        self.number = number

    def validate(self, expiration: str, holder: str, cvc: str) -> bool:
        """
        Validate card details against stored CSV data.
        """
        card_data = {
            "number": self.number,
            "expiration": expiration,
            "holder": holder,
            "cvc": cvc,
        }
        return card_data in df_cards


class SecureCreditCard(CreditCard):
    """
    Adds password authentication on top of CreditCard.
    """

    def authenticate(self, given_password: str) -> bool:
        password = df_cards_security.loc[
            df_cards_security["number"] == self.number, "password"
        ].squeeze()

        return password == given_password


class SpaTicket:
    """
    Generates a SPA reservation ticket.
    """

    def __init__(self, customer_name: str, hotel_object: Hotel):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self) -> str:
        return f"""
Thank you for your SPA reservation!

SPA Booking Details:
Customer Name: {self.customer_name}
Hotel Name: {self.hotel.name}
"""


# ---------------- APPLICATION FLOW ----------------
print(df_hotels)

hotel_id = input("Enter the id of the hotel: ")
hotel = SpaHotel(hotel_id)

if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456")

    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()

            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_obj=hotel)
            print(reservation_ticket.generate())

            spa = input("Do you want to book a spa package? ")
            if spa.lower() == "yes":
                hotel.book_spa_package()
                spa_ticket = SpaTicket(customer_name=name, hotel_object=hotel)
                print(spa_ticket.generate())
        else:
            print("❌ Credit card authentication failed.")
    else:
        print("❌ There was a problem with your payment.")
else:
    print("❌ Hotel is not available.")
