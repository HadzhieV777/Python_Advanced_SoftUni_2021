# 02. Checkmate

KING = "K"
QUEEN = "Q"


def is_valid(r, c, board):
    if r in range(len(board)) and c in range(len(board)):
        return True
    return False


def find_all_attacking_queens(r, c, dir):
    queens = []
    for direction in dir:
        next_row = r + dir[direction][0]
        next_col = c + dir[direction][1]

        while is_valid(next_row, next_col, chess_board):
            if chess_board[next_row][next_col] == QUEEN:
                queens.append([next_row, next_col])
                break

            next_row += dir[direction][0]
            next_col += dir[direction][1]
    return queens


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_right": (-1, 1),
    "up_left": (-1, -1),
    "down_right": (1, 1),
    "down_left": (1, -1),
}

chess_board = [list(input().split()) for _ in range(8)]


all_attacking_queens = []
for row in range(len(chess_board)):
    for col in range(len(chess_board)):
        if chess_board[row][col] == KING:

            all_attacking_queens = find_all_attacking_queens(row, col, directions)


if all_attacking_queens:
    for el in all_attacking_queens:
        print(el)
else:
    print('The king is safe!')