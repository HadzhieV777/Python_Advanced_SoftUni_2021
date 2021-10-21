# 09. Miner

from collections import deque


def is_valid(r, c, matrix):
    if r in range(len(matrix)) and c in range(len(matrix)):
        return True
    return False


def find_miner_position(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == MINER:
                return r, c


def find_all_coals(matrix):
    coals_list = []

    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == COAL:
                coals_list.append((r, c))
    return coals_list


def move_the_miner(r, c, command):
    if command == "left":
        return r, c - 1
    if command == "up":
        return r - 1, c
    if command == "right":
        return r, c + 1
    if command == 'down':
        return r + 1, c


REGULAR_FIELD_POSITION = "*"
END_OF_THE_ROUTE = "e"
COAL = "c"
MINER = "s"

field_size = int(input())
moving_commands = deque(input().split())

field = [list(input().split()) for _ in range(field_size)]

miner_row, miner_col = find_miner_position(field)
coals = find_all_coals(field)
coals_count = len(find_all_coals(field))

collected_coals = 0
next_miner_row, next_miner_col = 0, 0
while not coals_count == collected_coals:

    if not moving_commands:
        print(f"{coals_count - collected_coals} pieces of coal left. ({next_miner_row}, {next_miner_col})")
        break

    current_command = moving_commands.popleft()
    next_miner_row, next_miner_col = move_the_miner(miner_row, miner_col, current_command)

    if not is_valid(next_miner_row, next_miner_col, field):
        continue

    if field[next_miner_row][next_miner_col] == END_OF_THE_ROUTE:
        print(f"Game over! ({next_miner_row}, {next_miner_col})")
        break

    if field[next_miner_row][next_miner_col] == COAL:
        collected_coals += 1

    field[miner_row][miner_col] = REGULAR_FIELD_POSITION
    miner_row, miner_col = next_miner_row, next_miner_col


if coals_count == collected_coals:
    print(f"You collected all coal! ({next_miner_row}, {next_miner_col})")