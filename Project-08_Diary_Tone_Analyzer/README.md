# 📓 Diary Tone Analyzer

A Streamlit web application that analyzes personal diary entries and visualizes emotional trends over time using Natural Language Processing (NLP).

The app uses NLTK's VADER sentiment analyzer to calculate positivity and negativity scores for each diary entry and displays them using interactive Plotly charts.

---

## 🚀 Features

- Reads diary entries from text files
- Performs sentiment analysis using VADER
- Tracks positivity and negativity over time
- Interactive visualizations with Plotly
- Fast performance using Streamlit caching

---

## 🛠 Tech Stack

- Python
- Streamlit
- NLTK (VADER Sentiment Analyzer)
- Plotly
- Pathlib

---

## 📂 Project Structure
```
project-root/
│
├── diary/
│ ├── 2024-01-01.txt
│ ├── 2024-01-02.txt
│ └── 2024-01-03.txt
│
├── main.py
├── requirements.txt
└── README.md
```
---


## 📄 Diary Directory Dependency

The application depends on text files stored inside the `diary/` directory.

### Requirements for diary files:

- Files must have a `.txt` extension  
- Each file represents one diary entry  
- File names are used as the x-axis labels (for example: `2024-01-01.txt`)  
- Content should be plain UTF-8 text  
- At least one file must exist for the app to render charts  

Example:

```
diary/
├── 2024-03-01.txt
├── 2024-03-02.txt
├── 2024-03-03.txt
```

Each file should contain natural language text describing the diary entry for that day.

---

## ⚙️ Installation

```bash
clone the repo
cd diary-tone-analyzer
pip install -r requirements.txt
```

---
## ▶️ Run the App
```bash
streamlit run app.py
```

After running, Streamlit will open the app in your browser automatically.

---

## 🧠 How It Works

1. Loads all .txt diary files from the diary folder.
2. Extracts text content from each file.
3. Uses NLTK VADER to compute sentiment scores.
4. Stores positivity and negativity values.
5. Displays trends using Plotly line charts.

---

## 📦 Dependencies

All dependencies are listed in requirements.txt:
- ```streamlit``` – Web UI framework
- ```plotly``` – Interactive charts
- ```nltk```– Sentiment analysis engine

The VADER lexicon is automatically downloaded when the app runs for the first time.

---

## 📚 Credits & Acknowledgements

Special thanks to all educators and contributors who share knowledge and make learning accessible. 🙏

---
⭐ If you like this project, give it a star!