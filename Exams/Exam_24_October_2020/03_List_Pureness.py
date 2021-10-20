# 03. List Pureness

from collections import deque

def best_list_pureness(numbers, k):
    data = {}
    numbers = deque(numbers)

    for rotation in range(k + 1):
        if rotation == len(numbers):
            break

        result = sum([index * number for index, number in enumerate(numbers)])
        data.update({rotation: result})
        numbers.appendleft(numbers.pop())

    max_pureness = max(data.values())
    for key, val in data.items():
        if max_pureness == val:
            return f"Best pureness {val} after {key} rotations"


# TEST 1
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


# TEST 2
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)


# TEST 3
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)