# 04. Maximal Sum

import sys
from io import StringIO

test_input1 = '''4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4
'''

test_input2 = '''5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5
'''


# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = 0
nested_matrix_row = 0
nested_matrix_col = 0
for r in range(rows - 2):
    for c in range(cols - 2):
        current_sum = matrix[r][c] + \
                      matrix[r][c + 1] + \
                      matrix[r][c + 2] + \
                      matrix[r + 1][c] + \
                      matrix[r + 1][c + 1] + \
                      matrix[r + 1][c + 2] + \
                      matrix[r + 2][c] + \
                      matrix[r + 2][c + 1] + \
                      matrix[r + 2][c + 2]
        if current_sum > max_sum:
            max_sum, nested_matrix_row, nested_matrix_col = current_sum, r, c

print(f"Sum = {max_sum}")


print(matrix[nested_matrix_row][nested_matrix_col],
      matrix[nested_matrix_row][nested_matrix_col + 1],
      matrix[nested_matrix_row][nested_matrix_col + 2])

print(matrix[nested_matrix_row + 1][nested_matrix_col],
      matrix[nested_matrix_row + 1][nested_matrix_col + 1],
      matrix[nested_matrix_row + 1][nested_matrix_col + 2])

print(matrix[nested_matrix_row + 2][nested_matrix_col],
      matrix[nested_matrix_row + 2][nested_matrix_col + 1],
      matrix[nested_matrix_row + 2][nested_matrix_col + 2])