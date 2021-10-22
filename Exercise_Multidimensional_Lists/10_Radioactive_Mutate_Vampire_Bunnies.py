# 10. Radioactive Mutate Vampire Bunnies

from collections import deque


def is_valid(r, c, matrix):
    if r in range(len(matrix)) and c in range(len(matrix[0])):
        return True
    return False


def read_matrix(r):
    matrix = []
    for row in range(r):
        row_elements = list(input())
        matrix.append(row_elements)
    return matrix


def find_player_position(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == PLAYER:
                return r, c


def find_all_bunnies(matrix):
    bunnies_list = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == BUNNY:
                bunnies_list.append((r, c))
    return bunnies_list


def move_the_player(r, c, direction):

    # left
    if direction == "L":
        return r, c - 1

    # up
    if direction == "U":
        return r - 1, c

    # right
    if direction == "R":
        return r, c + 1

    # down
    if direction == "D":
        return r + 1, c


def spread_bunnies(bunnies, matrix):
    for bunny_position in bunnies:
        bunny_row, bunny_col = int(bunny_position[0]), int(bunny_position[1])
        # left
        if is_valid(bunny_row, bunny_col - 1, matrix):
            matrix[bunny_row][bunny_col - 1] = BUNNY
        # up
        if is_valid(bunny_row - 1, bunny_col, matrix):
            matrix[bunny_row - 1][bunny_col] = BUNNY
        # right
        if is_valid(bunny_row, bunny_col + 1, matrix):
            matrix[bunny_row][bunny_col + 1] = BUNNY
        # down
        if is_valid(bunny_row + 1, bunny_col, matrix):
            matrix[bunny_row + 1][bunny_col] = BUNNY


BUNNY = "B"
PLAYER = "P"
FREE_SPACE = "."

sizes = [int(x) for x in input().split()]
rows_count, cols_count = sizes

field = read_matrix(rows_count)
player_row, player_col = find_player_position(field)
bunnies_positions = []

commands = deque([x for x in input()])

is_win = True

next_player_row, next_player_col = 0, 0
while True:
    current_command = commands.popleft()
    next_player_row, next_player_col = move_the_player(player_row, player_col, current_command)
    field[player_row][player_col] = FREE_SPACE

    bunnies_positions = find_all_bunnies(field)
    spread_bunnies(bunnies_positions, field)

    if not is_valid(next_player_row, next_player_col, field):
        break

    if field[next_player_row][next_player_col] == BUNNY:
        is_win = False
        break

    player_row, player_col = next_player_row, next_player_col


for elements in field:
    print(''.join(elements))

if is_win:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {next_player_row} {next_player_col}")