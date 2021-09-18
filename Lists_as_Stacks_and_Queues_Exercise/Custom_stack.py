s = []

s.append(1)
s.append(-1)
s.append(4)
s.append(55)

print(s[2])

print(s[-1])  # to check the last el
while s:
    print(s.pop())


class Stack:
    def __init__(self):
        self.internal_stack = []

    # to take a value
    def push(self, value):
        self.internal_stack.append(value)

    # to return a value
    def pop(self):
        return  self.internal_stack.pop()

    # to check which value is
    def peek(self):
        return  self.internal_stack[-1]