# 01. Scheduling

from collections import deque

sequence_of_numbers = [int(x) for x in input().split(", ")]
index_to_find = int(input())

cycles = deque(sorted([(sequence_of_numbers[index], index) for index in range(len(sequence_of_numbers))]))

count_of_moves = 0
while cycles:
    current_number, current_index = cycles.popleft()
    count_of_moves += current_number

    if current_index == index_to_find:
        print(count_of_moves)
        break