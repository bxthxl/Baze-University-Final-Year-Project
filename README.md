# AI-Enhanced CCTV Surveillance System
### Facial Recognition System using Python and OpenCV

![Python](https://img.shields.io/badge/Python-AI%20Project-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Status](https://img.shields.io/badge/status-academic%20project-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

This repository contains the implementation of an **AI-powered facial recognition surveillance system** developed as part of my **BSc Computer Science project at Baze University**.

The system uses **computer vision and machine learning techniques** to detect human faces in real time and recognize known identities using trained facial datasets.

---

## Project Overview

Modern surveillance systems are increasingly integrating **Artificial Intelligence** to improve monitoring, identity verification, and security.

This project demonstrates how **computer vision and machine learning** can be used to build a facial recognition system capable of:

- Detecting human faces from a live camera feed  
- Capturing facial datasets for training  
- Training a recognition model  
- Recognizing known individuals in real time  

The system simulates how **AI-enhanced CCTV surveillance** can be implemented in environments such as offices, campuses, and secure facilities.

---

## Key Features

- Real-time face detection using OpenCV  
- Facial dataset collection for training  
- Face recognition using trained models  
- Identity verification  
- Simple graphical interface for interaction  

---

## Project Structure

```
Baze-University-Final-Year-Project
│
├── dataset_creator.py      # Captures facial datasets from the camera
├── detector.py             # Handles real-time face detection
├── trainer.py              # Trains the facial recognition model
├── gui.py                  # Graphical user interface
├── main.py                 # Main application entry point
│
├── data/                   # Captured training image datasets
├── recognizer/             # Trained recognition models
└── unknown/                # Images not recognized by the system
```

---

## Technologies Used

- Python  
- OpenCV  
- Computer Vision  
- Machine Learning  
- Haar Cascade Classifiers  

---

## Installation

Clone the repository:

```bash
git clone https://github.com/bxthxl/Baze-University-Final-Year-Project.git
```

Navigate into the project directory:

```bash
cd Baze-University-Final-Year-Project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## Future Improvements

- Deep learning–based facial recognition models  
- Integration with CCTV camera systems  
- Web dashboard for monitoring  
- Cloud-based identity database  

---

## Author

**Bethel Eberechukwu George-Nwaeke**

Computer Scientist  
Software Developer | AI Systems Enthusiast  

GitHub: https://github.com/bxthxl
