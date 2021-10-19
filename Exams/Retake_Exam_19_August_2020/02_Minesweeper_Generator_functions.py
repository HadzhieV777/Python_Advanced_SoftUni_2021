# 02. Minesweeper Generator with functions

def is_valid(r, c, field):
    if r in range(len(field)) and c in range(len(field)):
        return True
    return False


def return_position():
    data = input()
    positions = data[1:-1]
    row, col = int(positions.split(", ")[0]), int(positions.split(", ")[1])
    return row, col


def place_the_bombs(mines, field):
    for _ in range(mines):
        row, col = return_position()
        field[row][col] = BOMB


def fill_the_free_space(size):
    for r in range(size):
        for c in range(size):
            if not mines_field[r][c] == BOMB:
                mines_field[r][c] = calculate_all_the_position_numbers(r, c, mines_field)


def calculate_all_the_position_numbers(r, c, field):
    count_of_bombs_around = 0
    # up
    if is_valid(r - 1, c, field):
        if field[r - 1][c] == BOMB:
            count_of_bombs_around += 1

    # up-left
    if is_valid(r - 1, c - 1, field):
        if field[r - 1][c - 1] == BOMB:
            count_of_bombs_around += 1

    # up-right
    if is_valid(r - 1, c + 1, field):
        if field[r - 1][c + 1] == BOMB:
            count_of_bombs_around += 1

    # left
    if is_valid(r, c - 1, field):
        if field[r][c - 1] == BOMB:
            count_of_bombs_around += 1

    # right
    if is_valid(r, c + 1, field):
        if field[r][c + 1] == BOMB:
            count_of_bombs_around += 1

    # down
    if is_valid(r + 1, c, field):
        if field[r + 1][c] == BOMB:
            count_of_bombs_around += 1

    # down-left
    if is_valid(r + 1, c - 1, field):
        if field[r + 1][c - 1] == BOMB:
            count_of_bombs_around += 1

    # down-right
    if is_valid(r + 1, c + 1, field):
        if field[r + 1][c + 1] == BOMB:
            count_of_bombs_around += 1

    return count_of_bombs_around


def print_the_field(field):
    for el in field:
        print(' '.join([str(x) for x in el]))


BOMB = "*"

field_size = int(input())
mines_field = [list(" " * field_size) for _ in range(field_size)]

number_of_mines = int(input())

place_the_bombs(number_of_mines, mines_field)
fill_the_free_space(field_size)

print_the_field(mines_field)