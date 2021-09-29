# 05. Alice in Wonderland

import sys
from io import StringIO

test_input1 = '''5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left
'''

test_input2 = '''7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right
'''


# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def is_outside(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


def get_next_position(direction, r, c):
    if direction == 'up':
        return r - 1, c
    if direction == 'down':
        return r + 1, c
    if direction == 'left':
        return r, c - 1
    if direction == 'right':
        return r, c + 1


TRAP = 'R'
ALICE = 'A'

wonderland_territory = int(input())

matrix = []

alice_row, alice_col = 0, 0
for row in range(wonderland_territory):
    elements = input().split()
    matrix.append(elements)
    for col in range(wonderland_territory):
        element = elements[col]
        if element == ALICE:
            alice_row, alice_col = row, col

tea_bags = 0
matrix[alice_row][alice_col] = '*'

while True:
    command = input()
    alice_row, alice_col = get_next_position(command, alice_row, alice_col)

    if is_outside(alice_row, alice_col, wonderland_territory):
        break

    cell_value = matrix[alice_row][alice_col]
    matrix[alice_row][alice_col] = '*'

    if cell_value == TRAP:
        break

    if cell_value.isdigit():
        tea_bags += int(cell_value)
        if tea_bags >= 10:
            break

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(' '.join(row))
