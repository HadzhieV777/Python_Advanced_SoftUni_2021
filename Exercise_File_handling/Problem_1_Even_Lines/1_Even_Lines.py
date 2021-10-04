import re

with open('text.txt') as file:
    lines = file.readlines()

for index, line in enumerate(lines):
    if not index % 2 == 0:
        continue

    line = re.sub('[-,.!?]', '@', line)
    line = " ".join(reversed(line.split()))

    print(line.strip())

