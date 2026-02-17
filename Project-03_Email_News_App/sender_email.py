import smtplib
import ssl

# -------------------- CONFIG --------------------
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
USERNAME = "<<SENDER_EMAIL_ADDRESS>>"
PASSWORD = "<<SENDER_EMAIL_APP_PASSWORD>>"


def send_email(receiver: str, message: bytes):
    """
    Send email using Gmail SMTP.

    Args:
        receiver (str): Receiver email address.
        message (bytes): Email content.
    """
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, receiver, message)


if __name__ == "__main__":
    send_email("test@example.com", b"Subject: Test\n\nHello!")