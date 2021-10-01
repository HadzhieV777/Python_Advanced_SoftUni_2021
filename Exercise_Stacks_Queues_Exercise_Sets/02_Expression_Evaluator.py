# 02. Expression Evaluator

from collections import deque

string_expression = deque(input().split())
sequence_of_numbers = deque([])

for character in string_expression:
    try:
        sequence_of_numbers.append(int(character))
    except ValueError:
        operator = character
        current_num = sequence_of_numbers.popleft()
        while sequence_of_numbers:
            next_number = sequence_of_numbers.popleft()
            current_num = eval(f'{current_num} {operator} {next_number}')

        current_num = int(current_num)
        sequence_of_numbers.append(current_num)
print(*sequence_of_numbers)
