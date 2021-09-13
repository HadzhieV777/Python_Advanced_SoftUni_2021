# 1. Reverse Numbers

chars = input()
s = []

for char in chars.split():
    s.append(char)

reversed_s = []
while s:
    print(s.pop(), end=" ")