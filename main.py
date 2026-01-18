import cv2 as cv
import time
from config import CameraConfig, AIConfig, ServoConfig
from vision.detector import ObjectDetector
from control.tracking import TrackerController
from control.serial_comm import SerialCommunicator


class TrackingSystem:
    def __init__(self):
        """Ініціалізація всіх компонентів системи"""
        print("Ініціалізація системи...")
        self.cap = cv.VideoCapture(CameraConfig.INDEX)
        self.detector = ObjectDetector()
        self.tracker = TrackerController()

        # 1. Додаємо підключення до Arduino
        self.serial = SerialCommunicator()

        self.is_running = True

        # Для розрахунку метрики FPS [cite: 32]
        self.prev_time = 0

    def process_frame(self):
        """Обробка одного кадру відеопотоку"""
        ret, frame = self.cap.read()
        if not ret:
            return False

        # Отримуємо РЕАЛЬНІ розміри кадру, який дає камера
        height, width, _ = frame.shape

        # Оновлюємо центр у трекері динамічно
        self.tracker.center_x = width // 2
        self.tracker.center_y = height // 2
        # Оновлюємо Deadzone (10% від реальної ширини)
        self.tracker.deadzone_x = width * 0.1
        self.tracker.deadzone_y = height * 0.1

        detection = self.detector.get_detections(frame)

        if detection:
            coords, conf = detection
            # 3. Розрахунок кутів
            pan, tilt, center = self.tracker.calculate_angles(coords)

            # 4. ВІДПРАВКА НА ARDUINO (те, чого не вистачало)
            if self.serial.connection:
                self.serial.send_angles(pan, tilt)

            self._draw_ui(frame, coords, conf, pan, tilt)

        # Розрахунок та вивід FPS для звіту [cite: 32]
        self._show_fps(frame)

        cv.imshow('Robotic Tracking System', frame)
        return True

    def _draw_ui(self, frame, coords, conf, pan, tilt):
        """Внутрішній метод для малювання графічних елементів"""
        x1, y1, x2, y2 = map(int, coords)
        cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f'ID: {AIConfig.TARGET_CLASS} Conf: {conf:.2f}'
        cv.putText(frame, label, (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv.putText(frame, f"Angles: P:{pan} T:{tilt}", (10, 30),
                   cv.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    def _show_fps(self, frame):
        """Обчислення швидкодії системи [cite: 32]"""
        curr_time = time.time()
        fps = 1 / (curr_time - self.prev_time)
        self.prev_time = curr_time
        cv.putText(frame, f"FPS: {int(fps)}", (10, 60),
                   cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    def run(self):
        print(f"Система запущена. Модель: {AIConfig.MODEL_PATH}")
        while self.is_running:
            if not self.process_frame() or cv.waitKey(1) & 0xFF == ord('q'):
                self.is_running = False

        self.cleanup()

    def cleanup(self):
        """Визволення ресурсів при завершенні"""
        print("Завершення роботи...")
        self.cap.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    app = TrackingSystem()
    app.run()