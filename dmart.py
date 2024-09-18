products = {"Rice": 40, "Sugar": 35, "Wheat": 50, "Milk": 25, "Oil": 120}
cart = {}


print("Welcome to DMart Billing System\nAvailable Products:")
for product, price in products.items():
    print(f"{product}: ₹{price}")


while True:
    item = input("\nEnter product name (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    if item in products:
        qty = int(input(f"Enter quantity for {item}: "))
        cart[item] = cart.get(item, 0) + qty
    else:
        print("Product not available. Choose from available products.")

if cart:
    total = 0
    print("\nYour Cart:")
    for item, qty in cart.items():
        item_total = products[item] * qty
        print(f"{item} (x{qty}) - ₹{products[item]} each: ₹{item_total}")
        total += item_total
    print(f"\nTotal Bill: ₹{total}\nThank you for shopping at DMart!")
else:
    print("Your cart is empty. Thank you for visiting!")