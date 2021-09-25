# 02. Diagonal Difference
import sys
from io import StringIO

test_input1 = '''3
11 2 4
4 5 6
10 8 -12
'''

test_input2 = '''4
-7 14 9 -20
3 4 9 21
-14 6 8 44
'''


# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def read_matrix(n):
    matrix = []
    for _ in range(n):
        row = [int(el) for el in input().split()]
        matrix.append(row)
    return matrix


n = int(input())
matrix = read_matrix(n)

main_diagonal = 0
for i in range(n):
    main_diagonal += (matrix[i][i])

secondary_diagonal = 0
for i in range(n):
    secondary_diagonal += matrix[len(matrix) - 1 -i][i]

print(abs(main_diagonal - secondary_diagonal))