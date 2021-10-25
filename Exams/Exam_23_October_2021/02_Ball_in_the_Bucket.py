# 02. Ball in the Bucket

def is_valid(r, c, matrix):
    if r in range(len(matrix)) and c in range(len(matrix)):
        return True
    return False


def get_turn():
    turn_string = input()
    vals = turn_string[1:-1].split(', ')
    return [int(val) for val in vals]


def collect_all_nums_from_bucket(r, c, matrix):
    score = 0
    for direction in directions:
        next_row = r + directions[direction][0]
        next_col = c + directions[direction][1]

        while is_valid(next_row, next_col, matrix):
            score += int(matrix[next_row][next_col])

            next_row += directions[direction][0]
            next_col += directions[direction][1]
    return score


directions = {
    "up": (-1, 0),
    "down": (1, 0),
}

BUCKET = "B"

board = [list(input().split()) for _ in range(6)]

scored_points = 0
for _ in range(3):
    row, col = get_turn()

    if is_valid(row, col, board):

        if board[row][col] == BUCKET:
            board[row][col] = 0
            scored_points += collect_all_nums_from_bucket(row, col, board)

        # else:
        #     scored_points += int(board[row][col])

if scored_points < 100:
    print(f"Sorry! You need {100 - scored_points} points more to win a prize.")
else:
    if 100 <= scored_points <= 199:
        print(f"Good job! You scored {scored_points} points, and you've won Football.")
    elif 200 <= scored_points <= 299:
        print(f"Good job! You scored {scored_points} points, and you've won Teddy Bear.")
    elif 300 <= scored_points:
        print(f"Good job! You scored {scored_points} points, and you've won Lego Construction Set.")
