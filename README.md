![Python](https://img.shields.io/badge/Python-AI%20Project-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Status](https://img.shields.io/badge/status-academic%20project-orange)

# Baze University Final Year Project
## AI-Enhanced Online Examination Proctoring System

This repository contains the implementation of my **BSc Computer Science final year project at Baze University**.

The project explores the use of **Artificial Intelligence and Computer Vision** to enhance the security and integrity of online examinations by integrating facial recognition and monitoring capabilities into a digital proctoring system.

---

## Project Overview

Online examinations present significant challenges related to **identity verification and cheating prevention**. Traditional proctoring methods are difficult to scale and can be unreliable in remote environments.

This project introduces an **AI-assisted proctoring system** capable of:

- Detecting faces in real time
- Capturing facial datasets
- Training a recognition model
- Verifying student identity during examination sessions

The system demonstrates how computer vision can support **secure digital assessments** in educational institutions.

---

## Key Features

- Face detection using Haar Cascade classifiers
- Facial dataset generation for identity training
- Facial recognition for identity verification
- Local training pipeline for recognition models
- Graphical interface for interacting with the system

---

## Project Structure
Baze-University-Final-Year-Project
│
├── dataset_creator.py # Captures and stores facial datasets
├── detector.py # Handles face detection logic
├── trainer.py # Trains the facial recognition model
├── gui.py # Graphical user interface
├── main.py # Entry point for the application
│
├── data/ # Training image datasets
├── recognizer/ # Trained recognition models
└── unknown/ # Images not recognized by the system
## Technologies Used

- **Python**
- **OpenCV**
- **Computer Vision**
- **Machine Learning (Face Recognition)**
- **Haar Cascade Classifiers**

---

## Installation

Clone the repository:
git clone https://github.com/bxthxl/Baze-University-Final-Year-Project.git

Navigate into the project folder:
cd Baze-University-Final-Year-Project

Install required dependencies:
pip install -r requirements.txt

Run the application:
python main.py

Academic Context

This project was developed as part of the BSc Computer Science program at Baze University, Abuja.

The objective was to explore how AI-driven surveillance and recognition systems can support secure digital examination environments.
