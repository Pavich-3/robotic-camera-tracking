class CameraConfig:
    INDEX = 0
    WIDTH = 640
    HEIGHT = 480
    CENTER_X = WIDTH // 2
    CENTER_Y = HEIGHT // 2


class AIConfig:
    MODEL_PATH = 'models/best.pt'  # Архітектура YOLOv8 [cite: 19]
    CONFIDENCE = 0.3  # Поріг впевненості 30% [cite: 31]
    TARGET_CLASS = 0  # Person
    # Зона нечутливості (Deadzone) 10% [cite: 33]
    DEADZONE_X = CameraConfig.WIDTH * 0.1
    DEADZONE_Y = CameraConfig.HEIGHT * 0.1


class ServoConfig:
    PAN_PIN = 9
    TILT_PIN = 10
    STEP = 2
    INITIAL_ANGLE = 90 # Те, чого не вистачало
    BAUD_RATE = 9600
    PORT = 'COM3' # Порт для Arduino