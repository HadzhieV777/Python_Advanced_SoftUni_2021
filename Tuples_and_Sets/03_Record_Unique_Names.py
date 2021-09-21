# 03. Record Unique Names
n = int(input())
unique_names = set()

for _ in range(n):
    names = input()
    unique_names.add(names)

for unique_name in unique_names:
    print(unique_name)


# 03. Record Unique Names with functions
def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines

def print_result(names):
    for name in names:
        print(name)

n = int(input())
names = input_to_list(n)

unique_names = set(names)
print_result(unique_names)
