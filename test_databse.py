import json

# Load product database
with open("products.json", "r") as file:
    products = json.load(file)

# Display all products
print("SMARTCART PRODUCT DATABASE")

for key, value in products.items():
    print("--------------------")
    print("Product:", value["name"])
    print("Price: Rs.", value["price"])
    