
https://github.com/user-attachments/assets/7d92f6c3-7891-40ec-9273-57c1a025a891
# Real-Time Intelligent Object Tracking System with IBVS Control 🤖📸

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/AI-YOLOv8-green.svg)](https://github.com/ultralytics/ultralytics)
[![Hardware](https://img.shields.io/badge/Hardware-Arduino_Nano_ESP32-orange.svg)](https://docs.arduino.cc/hardware/nano-esp32)

An advanced robotic platform for automatic real-time object tracking, developed as a Master's coursework project. The system integrates **YOLOv8** for high-speed computer vision and a custom **Image-Based Visual Servoing (IBVS)** proportional controller for precision 2-axis gimbal management.

---

## 📺 Project Resources
* **Demo Video:**


https://github.com/user-attachments/assets/95661f79-100e-442c-8e4b-1897504d7fcd


* **Presentation:** [View on Canva](https://www.canva.com/design/DAG-5S-Ft6U/4QBLoy_iUCWQungKTzG8AA/edit?utm_content=DAG-5S-Ft6U&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
* **Training Pipeline:** [Google Colab Notebook](https://colab.research.google.com/drive/1OrkmFTnaheO_BJKmo6nhvCjHu4rZ69vs?usp=sharing) (Includes automated experiment script)

---

## 🚀 Key Features
* **Custom AI Model:** Optimized **YOLOv8n** trained on a specialized dataset of 2,107 images with manual annotation and heavy augmentation.
* **Control Theory:** Implemented **IBVS (Image-Based Visual Servoing)** to map image coordinates directly to servo velocities, ensuring smooth tracking without oscillations.
* **Performance:** Achieves a stable **30 FPS** on 720p streams with a detection confidence of **0.69**.
* **Embedded Implementation:** Hardware control via **Arduino Nano ESP32** with optimized serial communication.

---

## 🏗️ Hardware Setup
* **Microcontroller:** Arduino Nano ESP32
* **Actuators:** 2x MG90S Servos (Pan/Tilt Gimbal)
* **Sensor:** 720p USB Camera
