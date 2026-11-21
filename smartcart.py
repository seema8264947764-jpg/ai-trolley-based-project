import cv2
import json
from ultralytics import YOLO

# Load AI model
model = YOLO("yolov8n.pt")

# Load product database
with open("products.json", "r") as file:
    products = json.load(file)

# Shopping cart
cart = {}
total = 0

# Start camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not available!")
    exit()

print("SMARTCART AI STARTED!")

while True:

    success, frame = camera.read()

    if not success:
        break

    results = model(frame, verbose=False)

    detected_product = None

    for result in results:
        for box in result.boxes:

            class_id = int(box.cls[0])
            product_name = model.names[class_id]

            if product_name in products:
                detected_product = product_name
                break

        if detected_product:
            break

    # Display detected product
    if detected_product:

        name = products[detected_product]["name"]
        price = products[detected_product]["price"]

        cv2.putText(
            frame,
            f"{name} - Rs.{price}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f"Total Bill: Rs.{total}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    cv2.imshow("SMARTCART AI", frame)

    key = cv2.waitKey(1) & 0xFF

    # Press A to add detected product
    if key == ord('a') and detected_product:

        name = products[detected_product]["name"]
        price = products[detected_product]["price"]

        if name not in cart:
            cart[name] = {
                "price": price,
                "quantity": 0
            }

        cart[name]["quantity"] += 1
        total += price

        print(name, "added to cart!")

    # Press Q to exit
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

print("\n===== FINAL BILL =====")

for name, item in cart.items():
    subtotal = item["price"] * item["quantity"]

    print(name)
    print("Quantity:", item["quantity"])
    print("Price:", item["price"])
    print("Subtotal:", subtotal)

print("----------------------")
print("TOTAL BILL: Rs.", total)