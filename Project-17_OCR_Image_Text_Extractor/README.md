# OCR Image Text Extractor

A simple Python project that extracts text from images using **Tesseract OCR** and saves the extracted content into a text file.

This project processes all `.jpg` images in a folder and compiles their recognized text into a single output file.

---

## 📌 Features

- Extract text from multiple images automatically
- Supports batch processing of `.jpg` files
- Uses **Tesseract OCR** for accurate text recognition
- Saves extracted results in a structured text file
- Lightweight and beginner-friendly project

---

## 🛠 Technologies Used

- Python
- Pillow (PIL)
- pytesseract
- Tesseract OCR Engine

---

## 📂 Project Structure
```text
project-folder/
│
├── images/ # Folder containing input images
│ ├── image1.jpg
│ ├── image2.jpg
│
├── main.py # Main Python script
├── file.txt # Output file with extracted text
└── README.md # Project documentation
```


---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ocr-image-text-extractor.git
cd ocr-image-text-extractor
```
2. Install dependencies
```bash
pip install pillow pytesseract
```
3. Install Tesseract OCR

Tesseract must be installed on your system.

Mac
```bash
brew install tesseract
```
Ubuntu
```bash
sudo apt install tesseract-ocr
```
Windows

Download from:
https://github.com/tesseract-ocr/tesseract

After installation, add Tesseract to your system PATH.

---
## ▶️ How to Run the Project

1. Place all .jpg images inside the images folder.

Example:

```text
images/
student1.jpg
student2.jpg
student3.jpg
```

2. Run the Python script:
```bash
python app.py
```
The extracted text will be saved in:
```bash
file.txt
```
---
## 📄 Example Output

```text
File: student1.jpg
John Doe
Math: 85
Science: 90

**************************************************

File: student2.jpg
Jane Smith
Math: 88
Science: 92

**************************************************
```

## 📚 Credits & Acknowledgements

Special thanks to all educators and contributors who share knowledge and make learning accessible. 🙏

---

⭐ If you like this project, give it a star!
