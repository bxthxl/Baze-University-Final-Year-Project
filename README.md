# AI-Enhanced CCTV Surveillance System
### Facial Recognition using Python and OpenCV

![Python](https://img.shields.io/badge/Python-AI-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-ComputerVision-green)
![Status](https://img.shields.io/badge/status-academic--project-orange)

This repository contains an **AI-powered facial recognition surveillance system** developed using **Python and OpenCV**.

The system detects human faces in real time, captures facial datasets, trains a recognition model, and identifies individuals using computer vision techniques.

This project demonstrates how **AI-enhanced CCTV systems can be used for identity recognition and monitoring**.

---

# Project Overview

Traditional CCTV systems only record footage without understanding what is happening in the scene.

This project enhances surveillance systems by introducing **facial recognition capabilities**, allowing the system to identify individuals from a trained dataset.

The system performs the following tasks:

- Detects faces using **Haar Cascade classifiers**
- Captures facial images to build a dataset
- Trains a recognition model
- Recognizes faces from a live camera feed

---

# Key Features

- Real-time face detection
- Facial dataset generation
- Face recognition using trained models
- Identity verification
- Graphical user interface for system interaction

---

# Project Structure

```
Baze-University-Final-Year-Project
│
├── dataset_creator.py              # Captures facial datasets
├── detector.py                     # Face detection logic
├── trainer.py                      # Model training script
├── gui.py                          # Graphical user interface
├── main.py                         # Main application entry point
│
├── Face Detection.bat              # Script to launch the system
│
├── haarcascade_eye.xml             # Eye detection model
├── haarcascade_frontalface_default.xml   # Face detection model
├── haarcascade_profileface.xml     # Profile face detection model
│
├── data/                           # Captured training image dataset
├── recognizer/                     # Trained recognition model
├── unknown/                        # Images not recognized by the system
│
├── requirement.txt                 # Project dependencies
├── face_recognition.db             # Local recognition database
└── README.md                       # Project documentation
```

---

# Technologies Used

- Python
- OpenCV
- Computer Vision
- Machine Learning
- Haar Cascade Classifiers

---

# Installation

Clone the repository

```bash
git clone https://github.com/bxthxl/Baze-University-Final-Year-Project.git
```

Navigate to the project directory

```bash
cd Baze-University-Final-Year-Project
```

Install required dependencies

```bash
pip install -r requirement.txt
```

Run the system

```bash
python main.py
```

Or launch using the batch file

```bash
Face Detection.bat
```

---

# Future Improvements

Possible improvements for this project include:

- Deep learning–based facial recognition models
- Integration with real CCTV camera systems
- Web dashboard for monitoring
- Cloud-based identity database
- Multi-camera surveillance support

---

# Author

**Bethel Eberechukwu George-Nwaeke**

Computer Scientist  
Software Developer | AI Systems Enthusiast  

GitHub: https://github.com/bxthxl
