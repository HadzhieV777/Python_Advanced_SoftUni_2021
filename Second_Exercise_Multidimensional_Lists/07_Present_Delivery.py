# 07. Present Delivery
import sys
from io import StringIO

test_input1 = '''5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning
'''

test_input2 = '''3
4
- - - -
V - X -
- V C V
- - - S
left
up
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def is_outside(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


def get_next_position(direction, r, c):
    if direction == 'up':
        return r - 1, c
    if direction == 'down':
        return r + 1, c
    if direction == 'left':
        return r, c - 1
    if direction == 'right':
        return r, c + 1


def get_houses_in_range(size, r, c):
    houses = []
    if not is_outside(r - 1, c, size):
        houses.append([r - 1, c])
    if not is_outside(r + 1, c, size):
        houses.append([r + 1, c])
    if not is_outside(r, c - 1, size):
        houses.append([r, c - 1])
    if not is_outside(r, c + 1, size):
        houses.append([r, c + 1])
    return houses


SANTA = "S"
NAUGHTY_KID = "X"
GOOD_KID = "V"
COOKIES = "C"
END_COMMAND = "Christmas morning"

presents = int(input())
neighbourhood_size = int(input())

matrix = []

santa_row, santa_col = 0, 0
initialy_good_kids = 0
good_kids_count = 0

for row in range(neighbourhood_size):
    elements = input().split()
    matrix.append(elements)
    for col in range(neighbourhood_size):
        element = elements[col]
        if element == SANTA:
            santa_row, santa_col = row, col
        elif element == GOOD_KID:
            initialy_good_kids += 1

good_kids_count = initialy_good_kids

while True:
    command = input()

    if command == END_COMMAND:
        break

    next_santa_row, next_santa_col = get_next_position(command, santa_row, santa_col)
    if matrix[next_santa_row][next_santa_col] == GOOD_KID:
        good_kids_count -= 1
        presents -= 1
        matrix[next_santa_row][next_santa_col] = '-'

    elif matrix[next_santa_row][next_santa_col] == COOKIES:
        houses_in_range = get_houses_in_range(neighbourhood_size, next_santa_row, next_santa_col)
        for row, col in houses_in_range:
            if matrix[row][col] == NAUGHTY_KID:
                presents -= 1
            if matrix[row][col] == GOOD_KID:
                presents -= 1
                good_kids_count -= 1
            matrix[row][col] = '-'

            if presents == 0:
                break
    matrix[santa_row][santa_col] = '-'
    matrix[next_santa_row][next_santa_col] = SANTA
    santa_row, santa_col = next_santa_row, next_santa_col

    if presents == 0:
        break

if presents == 0 and good_kids_count > 0:
    print('Santa ran out of presents!')

for row_elements in matrix:
    print(' '.join(row_elements))

if good_kids_count == 0:
    print(f"Good job, Santa! {initialy_good_kids} happy nice kid/s.")
else:
    print(f"No presents for {good_kids_count} nice kid/s.")