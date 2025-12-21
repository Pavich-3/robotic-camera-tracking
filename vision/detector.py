from ultralytics import YOLO
# Імпортуємо конкретний клас налаштувань для ШІ
from config import AIConfig


class ObjectDetector:
    """
    Клас для інтелектуальної детекції об'єктів за допомогою YOLOv8[cite: 19].
    Забезпечує знаходження об'єктів у відеопотоці в реальному часі[cite: 6].
    """

    def __init__(self):
        # Використовуємо шлях до моделі з конфігурації [cite: 20]
        self.model = YOLO(AIConfig.MODEL_PATH)
        # Клас об'єкта, який потрібно відстежувати (наприклад, 0 для людини)
        self.class_id = AIConfig.TARGET_CLASS

    def get_detections(self, frame):
        """
        Аналізує кадр та повертає координати цілі.
        :param frame: кадр з відеопотоку
        :return: кортеж (координати, впевненість) або None
        """
        # Виконання детекції з вимкненим виводом у консоль (verbose=False)
        results = self.model(frame, verbose=False)[0]
        target = None

        for box in results.boxes:
            # Перевірка класу об'єкта та порогу впевненості з AIConfig
            if int(box.cls[0]) == self.class_id and box.conf[0] > AIConfig.CONFIDENCE:
                # Отримання координат bounding box (x1, y1, x2, y2)
                coords = box.xyxy.cpu().numpy()[0]
                # Отримання метрики впевненості для звіту [cite: 31]
                conf = box.conf[0].item()
                target = (coords, conf)

                # Повертаємо перший знайдений об'єкт для стабільності трекінгу
                break

        return target