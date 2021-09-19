# 02. Matching Parentheses
arithmetic_expression = input()
matching_parentheses = []

for index in range(len(arithmetic_expression)):
    element = arithmetic_expression[index]

    if element == "(":
        matching_parentheses.append(index)

    elif element == ")":
        left_parentheses = matching_parentheses.pop()
        print(arithmetic_expression[left_parentheses:index + 1])