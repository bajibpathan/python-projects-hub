import requests
from sender_email import send_email

# -------------------- CONFIG --------------------
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "<<YOUR_API_TOKEN>>"

QUERY_PARAMS = {
    "q": "tesla",
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": API_KEY
}

RECEIVER_EMAIL = "<<RECEIVER_EMAIL_ADDRESS>>"
SUBJECT = "Today's News Update"


# -------------------- HELPERS --------------------
def fetch_news(params: dict) -> list:
    """
    Fetch news articles from NewsAPI.

    Args:
        params (dict): Query parameters for API.

    Returns:
        list: List of articles.
    """
    response = requests.get(NEWS_API_ENDPOINT, params=params, timeout=10)
    response.raise_for_status()
    return response.json().get("articles", [])


def build_email_body(articles: list, limit: int = 10) -> bytes:
    """
    Build email content from articles.

    Args:
        articles (list): List of news articles.
        limit (int): Max articles to include.

    Returns:
        bytes: Encoded email message.
    """
    lines = []

    for article in articles[:limit]:
        title = article.get("title")
        desc = article.get("description")
        url = article.get("url")

        if title and desc:
            lines.append(f"{title}\n{desc}\n{url}\n")

    body_text = f"Subject: {SUBJECT}\n\n" + "\n".join(lines)
    return body_text.encode("utf-8")


# -------------------- MAIN FLOW --------------------
def main():
    """
    Main execution flow.
    """
    articles = fetch_news(QUERY_PARAMS)
    message = build_email_body(articles)
    send_email(RECEIVER_EMAIL, message)


if __name__ == "__main__":
    main()