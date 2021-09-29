# 04. Easter Bunny
import sys
from io import StringIO

test_input1 = '''5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0
'''

test_input2 = '''8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def is_inside(r, c, matrix_size):
    return 0 <= r < matrix_size and 0 <= c < matrix_size


size = int(input())

matrix = []

bunny_row, bunny_col = 0, 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == 'B':
            bunny_row, bunny_col = row, col

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

max_collected_eggs = float('-inf')

best_direction = ''
best_path = []

for direction, step in directions.items():

    eggs = 0
    current_row, current_col = bunny_row, bunny_col
    path = []

    while is_inside(current_row, current_col, size):
        current_row, current_col = step(current_row, current_col)

        if not is_inside(current_row, current_col, size):
            break

        if matrix[current_row][current_col] == 'X':
            break

        eggs += int(matrix[current_row][current_col])
        path.append([current_row, current_col])

    if eggs > max_collected_eggs:
        max_collected_eggs, best_direction, best_path = eggs, direction, path


print(best_direction)
for step in best_path:
    print(step)
print(max_collected_eggs)