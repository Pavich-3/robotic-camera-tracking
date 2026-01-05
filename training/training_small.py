from ultralytics import YOLO
from roboflow import Roboflow
import os

rf = Roboflow(api_key="ctA8XVslMV4jDn0HxNrE")
project = rf.workspace("coco-oshnc").project("pen-tracking-coursework")
version = project.version(3)
dataset = version.download("yolov8")

# Завантажуємо Small модель (вона має більше шарів та параметрів)
model = YOLO('../models/yolov8s.pt')


model_v4 = YOLO('../models/yolov8s.pt') # Використовуємо Small версію
model_v4.train(
    data='/content/Pen-Tracking-Coursework-3/data.yaml',
    epochs=100,
    imgsz=640,
    name='v4_small_accurate'
)