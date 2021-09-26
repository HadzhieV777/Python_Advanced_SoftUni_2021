# 05. Matrix of Palindromes
import sys
from io import StringIO

test_input1 = '''4 6
'''

test_input2 = '''3 2
'''


# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


rows, cols = [int(x) for x in input().split()]


for r in range(rows):
    for c in range(cols):
        print(f'{chr(97 + r)}{chr(97 + r + c)}{chr(97 + r)}', end=' ')
    print()