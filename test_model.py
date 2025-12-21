import cv2 as cv
from ultralytics import YOLO
import os
import config

# 1. Завантаження твоєї навченої моделі
# Шлях до файлу, який ти завантажив з Colab
MODEL_PATH = 'models/best.pt'

if not os.path.exists(MODEL_PATH):
    print(f"Помилка: Файл {MODEL_PATH} не знайдено.")
    exit()

model = YOLO(MODEL_PATH)


def test_inference():
    """Перевірка моделі на папці з тестовими зображеннями"""
    # Створи папку test_samples та поклади туди 5-10 фото,
    # які ТИ НЕ ВИКОРИСТОВУВАВ для навчання.
    test_images_dir = 'dataset_with_generator/dataset/test/images'

    if not os.path.exists(test_images_dir):
        print(f"Створи папку {test_images_dir} та додай туди тестові фото.")
        return

    print("--- ЗАПУСК ТЕСТУВАННЯ ---")

    for img_name in os.listdir(test_images_dir):
        img_path = os.path.join(test_images_dir, img_name)

        if not img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        # Виконання детекції (Inference)
        results = model(img_path)[0]

        # Отримання зображення з намальованими рамками
        annotated_frame = results.plot()

        # Візуалізація результату
        cv.imshow(f"Test: {img_name}", annotated_frame)

        print(f"Файл {img_name}: знайдено {len(results.boxes)} об'єктів.")

        # Натисніть будь-яку клавішу для переходу до наступного фото
        # Натисніть 'q' для виходу
        if cv.waitKey(0) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()


if __name__ == "__main__":
    test_inference()