# control/tracking.py
from config import CameraConfig, AIConfig, ServoConfig


class TrackerController:
    """
    Клас інтелектуального керування платформою.
    Реалізує алгоритм зворотного зв'язку між координатами об'єкта та кутами приводів.
    """

    def __init__(self):
        # Початкові кути з конфігурації сервоприводів
        self.pan_angle = ServoConfig.INITIAL_ANGLE
        self.tilt_angle = ServoConfig.INITIAL_ANGLE

        # Центр кадру для розрахунку відхилення (Error)
        self.center_x = CameraConfig.CENTER_X
        self.center_y = CameraConfig.CENTER_Y

    def calculate_angles(self, target_coords):
        """
        Розрахунок нових кутів на основі положення об'єкта.
        :param target_coords: (x1, y1, x2, y2) від детектора
        :return: (pan, tilt, target_center)
        """
        x1, y1, x2, y2 = map(int, target_coords)
        target_x = (x1 + x2) // 2
        target_y = (y1 + y2) // 2

        # 1. Горизонтальне керування (Pan)
        # Якщо центр об'єкта лівіше зони нечутливості — повертаємо камеру ліворуч
        if target_x < self.center_x - AIConfig.DEADZONE_X:
            self.pan_angle += ServoConfig.STEP
        # Якщо правіше — праворуч
        elif target_x > self.center_x + AIConfig.DEADZONE_X:
            self.pan_angle -= ServoConfig.STEP

        # 2. Вертикальне керування (Tilt)
        if target_y < self.center_y - AIConfig.DEADZONE_Y:
            self.tilt_angle += ServoConfig.STEP
        elif target_y > self.center_y + AIConfig.DEADZONE_Y:
            self.tilt_angle -= ServoConfig.STEP

        # 3. Обмеження (Clamping)
        # Сервоприводи працюють у діапазоні [0, 180] градусів
        self.pan_angle = max(0, min(180, self.pan_angle))
        self.tilt_angle = max(0, min(180, self.tilt_angle))

        return self.pan_angle, self.tilt_angle, (target_x, target_y)