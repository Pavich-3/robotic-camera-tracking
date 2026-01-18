import pandas as pd
from pathlib import Path
from ultralytics import YOLO


def final_benchmark():
    # Автоматичне визначення кореневої папки проєкту
    ROOT = Path(__file__).resolve().parent.parent
    MODELS_DIR = ROOT / "models_v3"
    DATA_YAML = ROOT / "dataset_with_generator" / "dataset" / "data.yaml"

    model_files = {
        "v1_best": MODELS_DIR / "v1_best.pt",
        "v2_best": MODELS_DIR / "v2_best.pt",
        "v3_best": MODELS_DIR / "v3_best.pt",
        "v4_best": MODELS_DIR / "v4_best.pt",
        "v5_best": MODELS_DIR / "v5_best.pt",
        "v6_best": MODELS_DIR / "v6_best.pt",
        "v7_best": MODELS_DIR / "v7_best.pt",
        "v8_best": MODELS_DIR / "v8_best.pt",
        "v9_best": MODELS_DIR / "v9_best.pt",
        "v10_best": MODELS_DIR / "v10_best.onnx",
    }

    results = []

    for name, path in model_files.items():
        if not path.exists():
            print(f"Пропуск {name}: файл не знайдено за шляхом {path}")
            continue

        print(f"--- Тестування {name} ---")
        model = YOLO(str(path))
        # Проводимо валідацію
        metrics = model.val(data=str(DATA_YAML), split='val', verbose=False)

        results.append({
            "Конфігурація": name,
            "mAP50": round(metrics.box.map50, 4),
            "mAP50-95": round(metrics.box.map, 4),
            "Inference (ms)": round(metrics.speed['inference'], 2),
            "FPS": round(1000 / metrics.speed['inference'], 2)
        })

    df = pd.DataFrame(results)
    print("\n--- ПІДСУМКОВА ТАБЛИЦЯ ЕКСПЕРИМЕНТІВ ---")
    print(df.to_string(index=False))

    # Збереження результатів для курсової
    output_path = ROOT / "training" / "final_model_comparison_v3.csv"
    df.to_csv(output_path, index=False)
    print(f"\nРезультати збережено у: {output_path}")


if __name__ == "__main__":
    final_benchmark()