import cv2
import os
from dotenv import load_dotenv
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # "n" = nano

# Load environment variables from .env file
load_dotenv()

# URL RTSP
url = os.getenv('RTSP_URL')

# Open video capture
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Can't connect to DVR.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fail to receive frame.")
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    cv2.imshow('DVR Stream', annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
