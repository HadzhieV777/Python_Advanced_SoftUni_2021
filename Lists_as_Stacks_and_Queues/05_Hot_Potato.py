# 05. Hot Potato
from collections import deque

player = input().split()
step = int(input())

q = deque(player)

while len(q) > 1:
    # for _ in range(step - 1):
    #     q.append(q.popleft())
    q.rotate(-step + 1)
    print(f"Removed {q.popleft()}")


print(f"Last is {q.popleft()}")