# 02. Snake

def is_valid(r, c, field):
    if r not in range(len(field)) or c not in range(len(field[r])):
        return False
    return True


def find_snake(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "S":
                return r, c


def find_burrow(field):
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == "B":
                return r, c


def possible_moves(r, c, direction, field):
    if direction == "up":
        return r - 1, c
    if direction == "down":
        return r + 1, c
    if direction == "left":
        return r, c - 1
    if direction == "right":
        return r, c + 1


territory = [list(input()) for _ in range(int(input()))]
snake_row, snake_col = find_snake(territory)

eaten_food = 0
won = True
while eaten_food < 10:
    command = input()
    territory[snake_row][snake_col] = "."
    snake_row, snake_col = possible_moves(snake_row, snake_col, command, territory)
    if not is_valid(snake_row, snake_col, territory):
        print("Game over!")
        print(f"Food eaten: {eaten_food}")
        print('\n'.join([''.join(territory[r]) for r in range(len(territory))]))
        won = False
        break

    if territory[snake_row][snake_col] == "*":
        eaten_food += 1

    elif territory[snake_row][snake_col] == "B":
        territory[snake_row][snake_col] = "."
        snake_row, snake_col = find_burrow(territory)

    territory[snake_row][snake_col] = "S"

if won:
    print("You won! You fed the snake.")
    print(f"Food eaten: {eaten_food}")
    print('\n'.join([''.join(territory[r]) for r in range(len(territory))]))
