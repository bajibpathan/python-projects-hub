# 📷 Motion Detection Alert System

A Python-based computer vision application that detects motion using OpenCV and sends email alerts with captured images when an object appears and leaves the camera frame.

This project demonstrates real-time image processing, multithreading, automation, and alerting workflows.

---

## 🚀 Features

- Real-time webcam monitoring
- Motion detection using background subtraction
- Bounding box visualization
- Automatic image capture
- Email alerts with attachments
- Multithreaded processing
- Secure credential handling

---

## 🛠 Tech Stack

- Python 3.9+
- OpenCV
- SMTP / EmailMessage
- Threading
- Pathlib

---

## 📂 Project Structure
```text
project-root/
│
├── images/
├── main.py
├── emailing.py
├── README.md
└── requirements.txt
```
---
## 📦 Dependencies

All external dependencies are listed in `requirements.txt`:

- `opencv-python` – Computer vision and webcam processing

Other modules such as `smtplib`, `email`, `threading`, `time`, and `os` are part of the Python standard library and do not require installation.

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Set your email credentials:
```bash
export EMAIL_SENDER="your_email@gmail.com"
export EMAIL_PASSWORD="your_app_password"
export EMAIL_RECEIVER="receiver@gmail.com"
```

On Windows (PowerShell):
```powershell
setx EMAIL_SENDER "your_email@gmail.com"
setx EMAIL_PASSWORD "your_app_password"
setx EMAIL_RECEIVER "receiver@gmail.com"
```
---

## ▶️ Run the App
```bash
python main.py
Press q to exit.
```
---

## 🧠 How It Works
- Captures frames from webcam.
- Converts frames to grayscale and blurs them.
- Computes difference from background.
- Detects contours of moving objects.
- Draws bounding boxes.
- Saves images when motion is detected.
- Sends email when object leaves frame.
- Cleans old images automatically.

---

## 📚 Credits & Acknowledgements

Special thanks to all educators and contributors who share knowledge and make learning accessible. 🙏

---
⭐ If you like this project, give it a star!