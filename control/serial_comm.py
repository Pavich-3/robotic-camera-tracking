import serial
import time
from config import ServoConfig


class SerialCommunicator:
    def __init__(self):
        try:
            self.connection = serial.Serial(
                port=ServoConfig.PORT,
                baudrate=ServoConfig.BAUD_RATE,
                timeout=0.1
            )
            time.sleep(2)
            print(f"Підключено до {ServoConfig.PORT} зі швидкістю {ServoConfig.BAUD_RATE}")
        except serial.SerialException as e:
            print(f"Помилка підключення до серійного порту: {e}")
            self.connection = None

    def send_angles(self, pan, tilt):
        if self.connection and self.connection.is_open:
            # Форматуємо дані як рядок: "90,45\n"
            data = f"{int(pan),int(tilt)}\n"
            self.connection.write(data.encode())