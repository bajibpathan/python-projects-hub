import smtplib
import imghdr
import os
from email.message import EmailMessage


SENDER = os.getenv("EMAIL_SENDER")
PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER = os.getenv("EMAIL_RECEIVER")


def send_email(image_path):
    """
    Sends an email with the detected image as an attachment.
    """

    email_message = EmailMessage()
    email_message["Subject"] = "New Object Detected"
    email_message["From"] = SENDER
    email_message["To"] = RECEIVER
    email_message.set_content("An object was detected by your camera.")

    with open(image_path, "rb") as file:
        content = file.read()

    email_message.add_attachment(
        content,
        maintype="image",
        subtype=imghdr.what(None, content),
    )

    # Use context manager for safe connection handling
    with smtplib.SMTP("smtp.gmail.com", 587) as gmail:
        gmail.ehlo()
        gmail.starttls()
        gmail.login(SENDER, PASSWORD)
        gmail.send_message(email_message)
    print("Email sent successfully.")