# 03. Numbers Search

from collections import Counter


def numbers_searching(*args):
    smallest_number = min(args)
    biggest_number = max(args)

    consecutive_numbers = []

    for element in range(smallest_number, biggest_number + 1):
        consecutive_numbers.append(element)

    missing_number = 0

    for number in consecutive_numbers:
        if number not in args:
            missing_number += number

    appearance_count = Counter(args)
    list_of_duplicates = sorted([k for k, v in appearance_count.items() if v > 1])

    list_to_print = [missing_number, list_of_duplicates]

    return list_to_print


# print(numbers_searching(1, 2, 4, 2, 5, 4))
# print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
# print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))