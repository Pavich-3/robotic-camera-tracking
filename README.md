# Real-Time Intelligent Object Tracking System with IBVS Control 🤖📸

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/AI-YOLOv8-green.svg)](https://github.com/ultralytics/ultralytics)
[![Hardware](https://img.shields.io/badge/Hardware-Arduino_Nano_ESP32-orange.svg)](https://docs.arduino.cc/hardware/nano-esp32)

An advanced robotic platform for automatic real-time object tracking, developed as a Master's coursework project. The system integrates **YOLOv8** for high-speed computer vision and a custom **Image-Based Visual Servoing (IBVS)** proportional controller for precision 2-axis gimbal management.

---

## 📺 Project Resources
* **Demo Video:** [Watch 30s Demo](ТВОЄ_ПОСИЛАННЯ_НА_ВІДЕО)
* **Presentation:** [View on Canva](ТВОЄ_ПОСИЛАННЯ_НА_CANVA)
* **Training Pipeline:** [Google Colab Notebook](ТВОЄ_ПОСИЛАННЯ_НА_COLAB) (Includes automated experiment script)

---

## 🚀 Key Features
* **Custom AI Model:** Optimized **YOLOv8n** trained on a specialized dataset of 2,107 images with manual annotation and heavy augmentation.
* **Control Theory:** Implemented **IBVS (Image-Based Visual Servoing)** to map image coordinates directly to servo velocities, ensuring smooth tracking without oscillations.
* **Performance:** Achieves a stable **30 FPS** on 720p streams with a detection confidence of **0.69**.
* **Embedded Implementation:** Hardware control via **Arduino Nano ESP32** with optimized serial communication.

---

## 🔬 Scientific Research & Experiments
The project involved a comprehensive comparative study of **12 different model configurations** to optimize the speed-accuracy trade-off for embedded hardware.

| Model ID | Architecture | $imgsz$ | Optimizer | Results (mAP / FPS) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **v2_nano_fast** | **Nano** | **320** | **AdamW** | **0.78 / 30 FPS** | **Selected** |
| v1_nano_std | Nano | 640 | Auto | 0.85 / 24 FPS | Latency issues |
| v4_small_acc | Small | 640 | AdamW | 0.92 / 12 FPS | Unstable Control |
| v7_nano_adamw | Nano | 320 | AdamW | 0.81 / 30 FPS | Competitive |

**Conclusion:** The Nano architecture with $imgsz=320$ was selected as the optimal solution to maintain the required sampling frequency for a stable feedback loop.

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



---

## 🛠️ Installation & Usage

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/your-username/your-repo.git](https://github.com/your-username/your-repo.git)
   cd your-repo
