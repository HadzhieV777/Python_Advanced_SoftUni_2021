# 1. Sum Matrix Elements

rows, cols = [int(el) for el in input().split(', ')]

matrix = []
sum_of_all = 0
for row in range(rows):
    matrix.append([int(el) for el in input().split(', ')])
    sum_of_all += sum(matrix[row])

print(sum_of_all)
print(matrix)