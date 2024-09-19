from products import products

def cart(item):
    cart=[]
    for i in products:
        if item==i:
            cart.append(i)
    
    return cart