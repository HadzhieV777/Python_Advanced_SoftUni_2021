# 02. Minesweeper Generator

def is_valid(r, c, field):
    if r in range(len(field)) and c in range(len(field)):
        return True
    return False


def read_matrix(n):
    matrix = []
    for row in range(n):
        matrix.append([None] * n)
    return matrix


def fill_the_field_with_nums(r, c, field):
    count_of_bombs = 0
    # up
    if is_valid(r - 1, c, field):
        if field[r - 1][c] == "*":
            count_of_bombs += 1

    # down
    if is_valid(r + 1, c, field):
        if field[r + 1][c] == "*":
            count_of_bombs += 1

    # left
    if is_valid(r, c - 1, field):
        if field[r][c - 1] == "*":
            count_of_bombs += 1

    # right
    if is_valid(r, c + 1, field):
        if field[r][c + 1] == "*":
            count_of_bombs += 1

    # up-left
    if is_valid(r - 1, c - 1, field):
        if field[r - 1][c - 1] == "*":
            count_of_bombs += 1

    # up-right
    if is_valid(r - 1, c + 1, field):
        if field[r - 1][c + 1] == "*":
            count_of_bombs += 1

    # down_left
    if is_valid(r + 1, c - 1, field):
        if field[r + 1][c - 1] == "*":
            count_of_bombs += 1

    # down-right
    if is_valid(r + 1, c + 1, field):
        if field[r + 1][c + 1] == "*":
            count_of_bombs += 1

    return count_of_bombs




matrix_size = int(input())
number_of_bombs = int(input())

matrix = read_matrix(matrix_size)


for _ in range(number_of_bombs):

    data = input()
    data_to_unpack = data[1:-1]
    row, col = int(data_to_unpack.split(", ")[0]), int(data_to_unpack.split(", ")[1])

    if is_valid(row, col, matrix):
        matrix[row][col] = "*"


for r in range(matrix_size):
    for c in range(matrix_size):

        if matrix[r][c] == None:
            count_of_bombs = fill_the_field_with_nums(r, c, matrix)
            matrix[r][c] = count_of_bombs


for el in matrix:
    print(" ".join([str(x) for x in el]))
