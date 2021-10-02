# 04. Honey
from collections import deque

bees = deque(int(el) for el in input().split())
nectars_values = deque(int(el) for el in input().split())
symbols = deque(input().split())

honey_made = 0
while bees:
    if nectars_values:
        if nectars_values[-1] >= bees[0]:
            current_nectar = nectars_values.pop()
            current_bee = bees.popleft()
            current_symbol = symbols.popleft()

            if current_symbol == "/" and current_nectar == 0:
                break

            honey_made += abs(eval(f'{current_bee} {current_symbol} {current_nectar}'))

        else:
            nectars_values.pop()
    else:
        break

print(f"Total honey made: {honey_made}")

if bees:
    bees_str = [str(el) for el in bees]
    print(f"Bees left: {', '.join(bees_str)}")

if nectars_values:
    nectars_values_str = [str(el) for el in nectars_values]
    print(f"Nectar left: {', '.join(nectars_values_str)}")