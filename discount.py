def apply_discount(cart,discount):
    desconto = (100 - discount) * 0,01
    for i in cart:
        cart[i] -= (cart[i] * desconto)
    return cart
