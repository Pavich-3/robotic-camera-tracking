# Real-Time Intelligent Object Tracking System with IBVS Control 🤖📸

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/AI-YOLOv8-green.svg)](https://github.com/ultralytics/ultralytics)
[![Hardware](https://img.shields.io/badge/Hardware-Arduino_Nano_ESP32-orange.svg)](https://docs.arduino.cc/hardware/nano-esp32)

An advanced robotic platform for automatic real-time object tracking, developed as a Master's coursework project. The system integrates **YOLOv8** for high-speed computer vision and a custom **Image-Based Visual Servoing (IBVS)** proportional controller for precision 2-axis gimbal management.

---

## 📺 Project Resources
* **Demo Video:** [Watch 30s Demo](ТВОЄ_ПОСИЛАННЯ_НА_ВІДЕО)
* **Presentation:** [View on Canva](https://www.canva.com/design/DAG-5S-Ft6U/4QBLoy_iUCWQungKTzG8AA/edit?utm_content=DAG-5S-Ft6U&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
* **Training Pipeline:** [Google Colab Notebook](https://colab.research.google.com/drive/1KoyhYKBslqNMCmJspQEDHHtCTEqwdPyt?usp=sharing) (Includes automated experiment script)

---

## 🚀 Key Features
* **Custom AI Model:** Optimized **YOLOv8n** trained on a specialized dataset of 2,107 images with manual annotation and heavy augmentation.
* **Control Theory:** Implemented **IBVS (Image-Based Visual Servoing)** to map image coordinates directly to servo velocities, ensuring smooth tracking without oscillations.
* **Performance:** Achieves a stable **30 FPS** on 720p streams with a detection confidence of **0.69**.
* **Embedded Implementation:** Hardware control via **Arduino Nano ESP32** with optimized serial communication.

---

## 🧠 Control Methodology
The tracking logic is based on minimizing the visual error vector $e(t)$ between the object's centroid and the frame center:

$$v_c = -\lambda \mathbf{L}_{\mathbf{e}^*}^+ (\mathbf{s}^* - \mathbf{s})$$

Where:
* **$v_c$**: Angular velocity command for servos.
* **$\lambda$**: Proportional gain (tuned to 0.1–0.5).
* **$\mathbf{s}^* - \mathbf{s}$**: Pixel error normalized by the focal length $f$.

---

## 🏗️ Hardware Setup
* **Microcontroller:** Arduino Nano ESP32
* **Actuators:** 2x MG90S Servos (Pan/Tilt Gimbal)
* **Sensor:** 720p USB Camera
