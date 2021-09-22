def read_matrix(row):
    mat = []
    for _ in range(row):
        mat.extend([int(el) for el in input().split(', ')])
    return mat


rows = int(input())
matrix = read_matrix(rows)
print(matrix)