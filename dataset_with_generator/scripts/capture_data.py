import cv2 as cv
import os
import time

SAVE_PATH = '../raw_images/'
CAPTURE_DELAY = 1.0  # seconds
OBJECT_NAME = 'pen'

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)
    print("Created directory: ", SAVE_PATH)


def main():
    cap = cv.VideoCapture(0)
    img_count = 0
    last_capture_time = time.time()

    print("Starting data capture")
    print("Stay in front of the camera with the object:", OBJECT_NAME)
    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        display_frame = frame.copy()
        cv.putText(display_frame, f'Images Captured: {img_count}', (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv.imshow('Data Capture', display_frame)

        current_time = time.time()
        if current_time - last_capture_time >= CAPTURE_DELAY:
            img_filename = f'{SAVE_PATH}{OBJECT_NAME}_{int(current_time)}.jpg'
            cv.imwrite(img_filename, frame)
            img_count += 1
            last_capture_time = current_time
            print(f'Captured image: {img_filename}')

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
    print("Data capture ended. Total images captured:", img_count)


if __name__ == "__main__":
    main()
