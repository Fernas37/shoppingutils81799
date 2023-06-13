def calculate_total_price(cart):
    total = 0

    for produto, preco in cart.items():
        total += preco

    return total
