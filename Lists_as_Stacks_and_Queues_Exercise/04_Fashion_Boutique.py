# 04. Fashion Boutique

clothes = list(map(int, input().split()))
rack_capacity = int(input())

counter_racks = 1

current_capacity = rack_capacity
while clothes:
    current_cloth = clothes.pop()

    if current_cloth <= current_capacity:
        current_capacity -= current_cloth
    else:
        counter_racks += 1
        current_capacity = rack_capacity
        current_capacity -= current_cloth
print(counter_racks)