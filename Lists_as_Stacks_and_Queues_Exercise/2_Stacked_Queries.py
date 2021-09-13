# 2. Stacked Queries

PUSH_COMMAND = "1"
DELETE_COMMAND = "2"
MAX_COMMAND = "3"
MIN_COMMAND = "4"

n = int(input())

stack = []
for _ in range(n):
    query = input()
    if PUSH_COMMAND in query:
        num_to_add = query.split()[1]
        stack.append(num_to_add)
    elif query == DELETE_COMMAND:
        if len(stack) > 0:
            stack.pop()
    elif query == MAX_COMMAND:
        if len(stack) > 0:
            print(max(stack))
    elif query == MIN_COMMAND:
        if len(stack) > 0:
            print((min(stack)))

reversed_stack = []
while stack:
    reversed_stack.append(stack.pop())

print(", ".join(reversed_stack))