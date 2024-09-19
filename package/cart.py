from shopping import cart

item=input("enter the item - ")
cart=cart(item)
for items in cart:
    print(f"{items} has been added to the cart")