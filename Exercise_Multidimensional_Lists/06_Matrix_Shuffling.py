# # 06. Matrix Shuffling
import sys
from io import StringIO

test_input1 = '''2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
'''

test_input2 = '''1 2
Hello World
0 0 0 1
swap 0 0 0 1
swap 0 1 0 0
END
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

END_COMMAND = 'END'

rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])


def is_valid_position(row1, col1, rows, cols):
    return 0 <= row1 < rows and 0 <= col1 < cols


while True:
    line = input()
    if line == END_COMMAND:
        break

    args = line.split()
    if not args[0] == 'swap' or not len(args) == 5:
        print('Invalid input!')
        continue
    row_one, col_one, row_two, col_two = [int(el) for el in args[1:]]

    if not is_valid_position(row_one, col_one, rows, cols) or not is_valid_position(row_two, col_two, rows, cols):
        print('Invalid input!')
        continue
    matrix[row_one][col_one], matrix[row_two][col_two] = matrix[row_two][col_two], matrix[row_one][col_one]
    for row_elements in matrix:
        print(' '.join([str(x) for x in row_elements]))