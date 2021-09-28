# 02. Matrix Modification
import sys
from io import StringIO

test_input1 = '''3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
'''

test_input2 = '''4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END
'''

# def read_matrix(r):
#     matrix = []
#     for _ in range(rows):
#         matrix.append([int(x) for x in input().split()])
#     return matrix

sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)


def is_invalid_position(size, row, col):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False

END_COMMAND = 'END'

size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == END_COMMAND:
        break

    data = line.split()
    command = data[0]
    row, col, value = [int(x) for x in data[1:]]
    if is_invalid_position(size, row, col):
        print("Invalid coordinates")
        continue
    if command == 'Add':
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for elements in matrix:
    print(" ".join([str(el) for el in elements]))