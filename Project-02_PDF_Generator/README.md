# 📄 Python PDF Generator

A simple **Python PDF Generator** that reads topics from a CSV file and creates structured PDF pages with headers, footers, and writing lines using the **FPDF** library.

This project is built for learning purposes and demonstrates file processing, layout control, and automation with Python.

---

## 🚀 Features

- Read data from CSV  
- Generate multiple pages per topic  
- Add headers and footers  
- Draw writing lines on each page  
- Fully automated PDF creation  

---

## 🛠 Tech Stack

- Python  
- Pandas  
- FPDF  

---

## 📂 Project Structure

```text
pdf-generator/
│
├── pdf_generator.py
├── topics.csv
├── output.pdf
└── README.md
```
---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install pandas fpdf
```

2. Prepare your CSV file (topics.csv):

```csv
Topic,Pages
Python Basics,2
Data Structures,3
OOP Concepts,1
```

3. Run the script:
```bash
python pdf_generator.py
```

The file output.pdf will be generated in the same folder.

---

## ✨ How It Works

- The script loads topics from topics.csv.
- Each topic generates one or more pages.
- The first page includes a header.
- All pages include writing lines and a footer.
- The PDF is saved automatically.

---

## 📚 Credits & Thanks

This project is created for learning and practice using inspiration from Python documentation, tutorials, and the open-source community.

🙏 Special thanks to educators and contributors who make learning accessible.