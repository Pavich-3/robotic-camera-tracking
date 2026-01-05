from ultralytics import YOLO
import os

# 1. Вибір базової моделі
# Ми використовуємо архітектуру YOLOv8n (nano) для балансу швидкості та точності [cite: 19, 20]
model = YOLO('yolov8n.pt')


def main():
    # 2. Запуск процесу навчання (Fine-tuning) [cite: 21, 49]
    results = model.train(
        data='dataset/data.yaml',   # Шлях до файлу конфігурації датасету
        epochs=100,                 # Кількість епох (ітерацій) навчання
        imgsz=640,                  # Роздільна здатність зображення
        batch=16,                   # Кількість зображень в одній групі
        name='pen_tracking_model',  # Назва папки з результатами
        device=0,                   # Використання GPU (якщо доступно)
        patience=20                 # Зупинка, якщо модель перестає покращуватися
    )

    # 3. Експорт навченої моделі в зручний формат
    model.export(format='onnx')


if __name__ == "__main__":
    main()