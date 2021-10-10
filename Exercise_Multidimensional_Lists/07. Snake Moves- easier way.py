# 07. Snake Moves- easier way

rows, cols = [int(x) for x in input().split()]

word = input()
word_index = 0

matrix = []
for row in range(rows):
    matrix.append([None] * cols)

    for col in range(cols):
        if  row % 2 == 0:
            matrix[row][col] = word[word_index]
        else:
            matrix[row][cols - 1 - col] = word[word_index]
        word_index = (word_index + 1) % len(word)

for element in matrix:
    print("".join(element))