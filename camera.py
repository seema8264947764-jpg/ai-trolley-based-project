import cv2

# Start laptop camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not available!")
    exit()

print("SmartCart AI Camera Started!")

while True:

    success, frame = camera.read()

    if not success:
        print("Camera error!")
        break

    cv2.putText(
        frame,
        "SmartCart AI",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("SmartCart AI Camera", frame)

    # Press Q to close camera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()