# 03. 2x2 Squares in Matrix
#
# import sys
# from io import StringIO
#
# test_input1 = '''3 4
# A B B D
# E B B B
# I J B B
# '''
#
# test_input2 = '''2 2
# a b
# c d
# '''
#
# test_input3 = '''5 4
# A A B D
# A A B B
# I J B B
# C C C G
# C C K P
# '''
#
# # sys.stdin = StringIO(test_input1)
# # sys.stdin = StringIO(test_input2)
# # sys.stdin = StringIO(test_input3)
#
#
# rows, cols = [int(n) for n in input().split()]
# matrix = [input().split() for _ in range(rows)]
# identical_sub_squares_count = 0
# for r in range(rows - 1):
#     for c in range(cols - 1):
#         if matrix[r][c] == matrix[r][c+1] == matrix[r+1][c] == matrix[r+1][c+1]:
#             identical_sub_squares_count += 1
#
# print(identical_sub_squares_count)