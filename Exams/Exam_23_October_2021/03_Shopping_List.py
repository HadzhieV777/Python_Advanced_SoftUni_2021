# 03. Shopping List

def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    shopping_cart = []
    for key, value in kwargs.items():
        data = [float(x) for x in value]
        price, quantity = data[0], data[1]
        total_price = price * quantity

        if total_price <= budget:
            shopping_cart.append(f"You bought {key} for {total_price:.2f} leva.")
            budget -= total_price

        if len(shopping_cart) == 5:
            return "\n".join(shopping_cart)

    return "\n".join(shopping_cart)
