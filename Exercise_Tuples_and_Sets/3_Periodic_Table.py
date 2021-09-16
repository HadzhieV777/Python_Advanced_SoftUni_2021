# 03. Periodic Table
n = int(input())

list_of_chemicals = []
for _ in range(n):
    chemicals = input().split()
    for chemical in chemicals:
        list_of_chemicals.append(chemical)

unique_chemicals = set(list_of_chemicals)

for chem in unique_chemicals:
    print(chem)