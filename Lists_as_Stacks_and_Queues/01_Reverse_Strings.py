# 01. Reverse Strings

text = input()

s = []

for el in text:
    s.append(el)

reversed_text = ""
while s:
    reversed_text += s.pop()
print(reversed_text)