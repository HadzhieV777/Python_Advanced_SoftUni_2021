# 01. Diagonals
import sys
from io import StringIO

test_input1 = '''3
1, 2, 3
4, 5, 6
7, 8, 9
'''

# sys.stdin = StringIO(test_input1)


def read_matrix(n):
    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


n = int(input())
matrix = read_matrix(n)


primary_diagonal = []
secondary_diagonal = []
for row_index in range(len(matrix)):
    primary_diagonal.append(matrix[row_index][row_index])
    secondary_diagonal.append(matrix[row_index][n - row_index - 1])

primary_diagonal_sum = sum(primary_diagonal)
secondary_diagonal_sum = sum(secondary_diagonal)

print(f'Primary diagonal: {", ".join([str(el) for el in primary_diagonal])}. Sum: {primary_diagonal_sum}')
print(f'Secondary diagonal: {", ".join([str(el) for el in secondary_diagonal])}. Sum: {secondary_diagonal_sum}')
