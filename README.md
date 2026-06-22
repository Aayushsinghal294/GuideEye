
# GuideEye - AI-Powered Assistive Vision System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Embedded-C51A4A?style=for-the-badge&logo=raspberrypi)
![OCR](https://img.shields.io/badge/OCR-Tesseract-orange?style=for-the-badge)
![TTS](https://img.shields.io/badge/Text--to--Speech-pyttsx3-purple?style=for-the-badge)

### AI-Powered Assistive Vision System for Visually Impaired Users

GuideEye leverages **Computer Vision**, **OCR**, **Face Recognition**, and **Text-to-Speech** to provide real-time spoken assistance, helping visually impaired users interact with their surroundings more independently.

</div>

---

## ✨ Features

- 📖 OCR-based text recognition
- 🔊 Real-time Text-to-Speech (TTS)
- 👤 Face recognition using DeepFace
- 📷 Live camera image processing
- ⚡ Raspberry Pi deployment
- 🤖 AI-powered assistive system for accessibility

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Computer Vision | OpenCV |
| OCR | Tesseract OCR |
| Face Recognition | DeepFace |
| Text-to-Speech | pyttsx3 |
| Hardware | Raspberry Pi, USB Camera |

---

## 🚀 System Workflow

```text
Camera Input
      │
      ▼
 Image Capture
      │
 ┌────┴────┐
 ▼         ▼
 OCR    Face Recognition
 │         │
 └────┬────┘
      ▼
 Information Processing
      ▼
 Text-to-Speech
      ▼
 Voice Guidance
```

---

## 📌 Key Functionalities

### 📖 OCR & Text Reading
- Captures text using the onboard camera.
- Extracts text using **Tesseract OCR**.
- Reads detected text aloud through **Text-to-Speech**.

### 👤 Face Recognition
- Detects and recognizes registered individuals.
- Uses **DeepFace** for facial recognition.
- Announces recognized users using voice feedback.

### 🔊 Text-to-Speech
- Converts extracted text into natural speech.
- Enables hands-free reading of books, documents, and signboards.
- Provides instant audio feedback for accessibility.

### 📷 Real-Time Image Processing
- Captures live camera frames.
- Processes images in real time.
- Delivers spoken guidance with minimal delay.

---

## 📂 Project Structure

```text
GuideEye/
│── Face Recognition/
│── Image To Speech/
│── OCR/
│── Images/
│── main.py
│── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/GuideEye.git
cd GuideEye
```

Install dependencies

```bash
pip install -r requirements.txt
```

Install Tesseract OCR

### Windows

Download and install:

https://github.com/UB-Mannheim/tesseract/wiki

### Ubuntu

```bash
sudo apt install tesseract-ocr
```

---

## ▶️ Run

```bash
python main.py
```
---

## 🎯 Applications

- Assistive technology for visually impaired users
- Smart accessibility devices
- AI-powered reading assistant
- Embedded AI systems
- Computer Vision applications

---
<img width="300" height="500" alt="WhatsApp Image 2026-01-15 at 11 39 01 PM" src="https://github.com/user-attachments/assets/2e0e5754-1ecf-4c66-8384-73db16f37ec7" />

## 🤝 Contributors

- **Shivansh Chaurasiya**
- **Aayush Singhal**

---


