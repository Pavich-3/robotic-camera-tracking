import time
import torch
from ultralytics import YOLO
import pandas as pd
from config import AIConfig
from pathlib import Path


def run_benchmark(model_path, model_name, data_path):
    model = YOLO(model_path)

    print(f"--- Запуск бенчмарку для моделі: {model_name} ---")
    metrics = model.val(data=data_path, verbose=False)
    map50 = metrics.box.map50

    # Обчислення FPS
    # Робимо 100 прогонів на порожному тензорі для об'єктивності
    dummy_input = torch.rand(1, 3, 640, 640) # Значення від 0 до 1
    if torch.cuda.is_available():
        model.to('cuda')
        dummy_input = dummy_input.to('cuda')

    start_time = time.time()
    iterations = 100
    for _ in range(iterations):
        model.predict(dummy_input, verbose=False)

    end_time = time.time()
    avg_inference_time = (end_time - start_time) / iterations
    fps = 1 / avg_inference_time

    return {
        "Модель": model_name,
        "mAP50": round(map50, 4),
        "FPS": round(fps, 2),
        "Час виводу (мс)": round(avg_inference_time * 1000, 2)
    }


if __name__ == "__main__":
    ROOT = Path(__file__).resolve().parents[1]
    DATA_YAML = ROOT / 'dataset_with_generator' / 'dataset' / 'data.yaml'

    results = [run_benchmark('yolov8n.pt', 'Base YOLOv8n', DATA_YAML),
               run_benchmark(ROOT / AIConfig.MODEL_PATH, 'Custom Fine-tuned Model', DATA_YAML)]

    df = pd.DataFrame(results)
    print("\n--- Результати Бенчмарку ---")
    print(df.to_string(index=False))

    df.to_csv('benchmark_results.csv', index=False)
