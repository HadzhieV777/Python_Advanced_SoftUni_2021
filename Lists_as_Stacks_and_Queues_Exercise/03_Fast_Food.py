# 03. Fast Food

from collections import deque

total_food_quantity = int(input())
orders = deque([int(el) for el in input().split()])

print(max(orders))
while orders:
    order = orders.popleft()

    if order <= total_food_quantity:
        total_food_quantity -= order
    else:
        orders.appendleft(order)
        break

if not orders:
    print("Orders complete")
else:
    remaining_orders = [str(el) for el in orders]
    print(f"Orders left: {' '.join(remaining_orders)}")