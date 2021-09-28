# 03. Knight Game
import sys
from io import StringIO

test_input1 = '''5
0K0K0
K000K
00K00
K000K
0K0K0
'''

test_input2 = '''2
KK
KK
'''

test_input3 = '''8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)


def is_valid_position_and_is_a_knight(chess_board, r, c):
    chess_board_size = len(chess_board)
    if r < 0 or c < 0 or r >= chess_board_size or c >= chess_board_size:
        return False
    return chess_board[r][c] == 'K'


def count_attacked_knights(chess_board, r, c):
    result = 0
    if is_valid_position_and_is_a_knight(chess_board, r - 2, c - 1):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r - 2, c + 1):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r + 2, c - 1):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r + 2, c + 1):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r - 1, c - 2):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r - 1, c + 2):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r + 1, c - 2):
        result += 1
    if is_valid_position_and_is_a_knight(chess_board, r + 1, c + 2):
        result += 1
    return result


board_size = int(input())

matrix = []

for _ in range(board_size):
    matrix.append(list(input()))

removed_knights = 0

while True:
    max_count, knight_row, knight_col = 0, 0, 0

    for r in range(board_size):
        for c in range(board_size):
            if matrix[r][c] == '0':
                continue
            count = count_attacked_knights(matrix, r, c)
            if count > max_count:
                max_count, knight_row, knight_col = count, r, c
    if max_count == 0:
        break
    matrix[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)