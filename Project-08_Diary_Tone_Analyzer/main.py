import streamlit as st
import plotly.express as px
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path


# Cache the analyzer so Streamlit doesn't recreate it on every rerun
@st.cache_resource
def get_analyzer():
    """
    Downloads the VADER lexicon (if not present) and
    returns a cached SentimentIntensityAnalyzer instance.
    """
    nltk.download("vader_lexicon", quiet=True)
    return SentimentIntensityAnalyzer()


# -------------------- UI SETUP --------------------
st.title("📓 Diary Tone Analyzer")


# -------------------- FILE LOADING --------------------
DIARY_PATH = Path("diary")

# Collect and sort all diary text files
file_paths = sorted(DIARY_PATH.glob("*.txt"))

# Extract file names (without extension) for x-axis labels
dates = [file.stem for file in file_paths]


# -------------------- ANALYSIS --------------------
analyzer = get_analyzer()

positive_scores = []
negative_scores = []

for file_path in file_paths:
    # Read diary entry safely
    text = file_path.read_text(encoding="utf-8")

    # Calculate sentiment scores using VADER
    scores = analyzer.polarity_scores(text)

    # Store only what we need
    positive_scores.append(scores["pos"])
    negative_scores.append(scores["neg"])


# -------------------- VISUALIZATION --------------------
st.subheader("😊 Positivity Trend")

pos_fig = px.line(
    x=dates,
    y=positive_scores,
    labels={"x": "Date", "y": "Positivity Score"},
    title="Diary Positivity Over Time",
)

st.plotly_chart(pos_fig, use_container_width=True)


st.subheader("😡 Negativity Trend")

neg_fig = px.line(
    x=dates,
    y=negative_scores,
    labels={"x": "Date", "y": "Negativity Score"},
    title="Diary Negativity Over Time",
)

st.plotly_chart(neg_fig, use_container_width=True)