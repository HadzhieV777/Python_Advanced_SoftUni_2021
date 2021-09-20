# 01. Count Same Values
sequence_of_numbers = input().split()

numbers_count = {}

for number in sequence_of_numbers:
    if number not in numbers_count:
        numbers_count[number] = 0
    numbers_count[number] += 1

for num, count in numbers_count.items():
    print(f'{float(num)} - {count} times')