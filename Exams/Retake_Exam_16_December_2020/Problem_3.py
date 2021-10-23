# Problem 3

def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    for row_index in range(2, n):
        triangle.append([])
        triangle[-1].append(1)

        for column_index in range(1, row_index):
            left = triangle[row_index - 1][column_index - 1]
            right = triangle[row_index - 1][column_index]
            triangle[-1].append(left + right)

        triangle[-1].append(1)
    return triangle

get_magic_triangle(5)