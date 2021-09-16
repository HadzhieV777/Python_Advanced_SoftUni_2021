# 02. Sets of Elements

def input_to_set(n_or_m,set_of):
    for _ in range(n_or_m):
        num = int(input())
        set_of.add(num)

def check_if_contains_in_both(set_of_n, set_of_m, list_of_elements):
    for el in set_of_n:
        if el in set_of_n and el in set_of_m:
            list_of_elements.append(el)


n, m = input().split()
n, m = int(n), int(m)

set_n, set_m = set(), set()
contains_in_both = []

input_to_set(n, set_n)
input_to_set(m, set_m)
check_if_contains_in_both(set_n, set_m, contains_in_both)
check_if_contains_in_both(set_m, set_n, contains_in_both )

contains_in_both = set(contains_in_both)
for number in contains_in_both:
    print(number)