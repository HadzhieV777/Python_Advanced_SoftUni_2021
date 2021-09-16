# 1. Unique Usernames
n = int(input())

usernames = []

for _ in range(n):
    username = input()
    usernames.append(username)

unique_username = set(usernames)
print("\