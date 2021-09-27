# 07. Snake Moves
def create_matrix_from_spaces(row, col):
    matrix = []
    for _ in range(row):
        matrix.append([])
        for _ in range(col):
            matrix[-1].append('')
    return matrix


n, m = [int(el) for el in input().split()]
text = input()

matrix = create_matrix_from_spaces(n, m)

text_index = 0
col = 0
for row in range(n):
    if row % 2 == 0:
        snake_direction = 1
    else:
        snake_direction = -1

    while 0 <= col < m:
        matrix[row][col] = text[text_index]
        if text_index + 1 == len(text):
            text_index = -1
        text_index += 1
        col += snake_direction
    col -= snake_direction


for i in range(len(matrix)):
    print(''. join(matrix[i]))
