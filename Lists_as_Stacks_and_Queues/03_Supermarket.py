# 03. Supermarket
from collections import deque
PAIND_COMMAND = 'Paid'
END_COMMAND = 'End'

customer_name = input()
q = deque()

while True:
    if customer_name == END_COMMAND:
        print(f"{len(q)} people remaining.")
        break

    elif customer_name == PAIND_COMMAND:
        while q:
            print(q.popleft())

    else:
        q.append(customer_name)

    customer_name = input()