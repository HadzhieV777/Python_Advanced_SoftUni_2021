# 6. Balanced Parentheses

sequence_of_parentheses = input()

is_balanced = True
stack = []

for parenthesis in sequence_of_parentheses:
    if parenthesis in '{[(':
        stack.append(parenthesis)

    elif parenthesis in ')]}':
        if len(stack) == 0:
            is_balanced = False

        opening_parenthesis = stack.pop()
        pair = f'{opening_parenthesis}{parenthesis}'

        if pair not in ['[]', '{}', '()']:
            is_balanced = False
            break

if is_balanced and len(stack) == 0:
    print('YES')
else:
    print('NO')
