from ultralytics import YOLO
import cv2

# Load AI model
model = YOLO("yolov8n.pt")

# Start camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not available!")
    exit()

print("SmartCart AI Detection Started!")

while True:

    success, frame = camera.read()

    if not success:
        print("Camera error!")
        break

    # Detect objects using AI
    results = model(frame)

    # Draw detection boxes
    output = results[0].plot()

    # Show camera
    cv2.imshow("SmartCart AI Detection", output)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()