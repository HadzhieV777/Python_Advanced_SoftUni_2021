# Problem 2

PLAYER = "P"
EMPTY_POSITION = "-"


def is_valid(r, c, field):
    if r in range(len(field)) and c in range(len(field)):
        return True
    return False


def find_player_position(field):
    for row in range(len(field)):
        for col in range(len(field)):
            if matrix[row][col] == PLAYER:
                return  row, col


def move_player(player_r, player_c, direction):
    if direction == "up":
        return player_r - 1, player_c
    if direction == "down":
        return player_r + 1, player_c
    if direction == "left":
        return player_r, player_c - 1
    if direction == "right":
        return player_r, player_c + 1


initial_string = input()

matrix = [list(input()) for _ in range(int(input()))]


player_row, player_col = find_player_position(matrix)

m = int(input())
next_player_row, next_player_col = 0, 0
for _ in range(m):
    command = input()

    next_player_row, next_player_col = move_player(player_row, player_col, command)

    if is_valid(next_player_row, next_player_col, matrix):
        matrix[player_row][player_col] = EMPTY_POSITION
        if matrix[next_player_row][next_player_col].isalpha():
            initial_string += matrix[next_player_row][next_player_col]
            matrix[next_player_row][next_player_col] = EMPTY_POSITION
        player_row, player_col = next_player_row, next_player_col
    else:
        if not initial_string == "":
            initial_string = initial_string[:-1]
    matrix[player_row][player_col] = PLAYER

print(initial_string)
for el in matrix:
    print("".join(el))