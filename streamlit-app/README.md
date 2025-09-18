# Car🚗 Damage Detection System

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Status](https://img.shields.io/badge/status-active-success)

A computer vision-based system that automatically detects and classifies damage to vehicles, specifically identifying breakages and crushes in the front and rear sections of cars.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Contributing](#contributing)


## About

The Car Damage Detection System is an AI-powered solution that helps automate vehicle damage assessment. Using deep learning and computer vision techniques, the system can:

- Detect whether a car has damage in the front or rear sections
- Classify the type of damage (breakage vs. crush)
- Identify normal/undamaged vehicle sections
- Provide assessment results that could be valuable for insurance claims, automotive repairs, and vehicle inspections

This project demonstrates the application of modern computer vision techniques to solve real-world problems in the automotive industry.

## Features

- **Dual Analysis**: Separate detection for front and rear vehicle sections
- **Damage Classification**: Distinguishes between breakages and crushes
- **Real-time Processing**: Capable of analyzing images quickly
- **Accuracy**: High precision in damage detection and classification
- **User-friendly**: Simple interface for uploading and analyzing car images


## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps
- **TO install the required packages**
```commandline
pip3 install -r requirements
```

## Usage
- **To Run the app use command** : 
```commandline
streamlit run app.py
```

## Model Details
**This system utilizes a convolutional neural network (CNN) architecture based on Transfer Learning:**

- Base Model: ResNet50 (pre-trained on ImageNet)
- Custom Layers: Added custom classification heads for front and rear damage detection
- Training Data: Curated dataset of car images with various damage types
- Accuracy: Achieves over 80% accuracy in damage classification


  
## Contributing

#### We welcome contributions to improve the Car Damage Detection System:

- Fork the project
- Create your feature branch (git checkout -b feature/AmazingFeature)
- Commit your changes (git commit -m 'Add some AmazingFeature')
- Push to the branch (git push origin feature/AmazingFeature)
- Open a Pull Request




