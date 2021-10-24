# 01. Aladdin's Gifts

from collections import deque


def check_the_sum(sum, gifts, material, magic_level):
    if 100 <= sum <= 199:
        gifts['Gemstone'] += 1
        material.pop()
        magic_level.popleft()

    elif 200 <= sum <= 299:
        gifts['Porcelain Sculpture'] += 1
        material.pop()
        magic_level.popleft()

    elif 300 <= sum <= 399:
        gifts['Gold'] += 1
        material.pop()
        magic_level.popleft()

    elif 400 <= sum <= 499:
        gifts['Diamond Jewellery'] += 1
        material.pop()
        magic_level.popleft()

    elif sum > 499:
        sum = sum // 2
        if sum < 100:
            if sum % 2 == 0:
                sum = (material[-1] * 2) + (magic_level[0] * 3)
                if 100 <= sum <= 199:
                    gifts['Gemstone'] += 1
                    material.pop()
                    magic_level.popleft()

                elif 200 <= sum <= 299:
                    gifts['Porcelain Sculpture'] += 1
                    material.pop()
                    magic_level.popleft()

                elif 300 <= sum <= 399:
                    gifts['Gold'] += 1
                    material.pop()
                    magic_level.popleft()

                elif 400 <= sum <= 499:
                    gifts['Diamond Jewellery'] += 1
                    material.pop()
                    magic_level.popleft()
                else:
                    material.pop()
                    magic_level.popleft()
            else:
                sum = (material[-1] * 2) + (magic_level[0] * 2)
                if 100 <= sum <= 199:
                    gifts['Gemstone'] += 1
                    material.pop()
                    magic_level.popleft()

                elif 200 <= sum <= 299:
                    gifts['Porcelain Sculpture'] += 1
                    material.pop()
                    magic_level.popleft()

                elif 300 <= sum <= 399:
                    gifts['Gold'] += 1
                    material.pop()
                    magic_level.popleft()

                elif 400 <= sum <= 499:
                    gifts['Diamond Jewellery'] += 1
                    material.pop()
                    magic_level.popleft()
                else:
                    material.pop()
                    magic_level.popleft()


        if 100 <= sum <= 199:
            gifts['Gemstone'] += 1
            material.pop()
            magic_level.popleft()

        elif 200 <= sum <= 299:
            gifts['Porcelain Sculpture'] += 1
            material.pop()
            magic_level.popleft()

        elif 300 <= sum <= 399:
            gifts['Gold'] += 1
            material.pop()
            magic_level.popleft()

        elif 400 <= sum <= 499:
            gifts['Diamond Jewellery'] += 1
            material.pop()
            magic_level.popleft()
        else:
            material.pop()
            magic_level.popleft()


materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

gifts_to_craft = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0,
}


is_win = False
while materials and magic_levels:
    current_material = materials[-1]
    current_magic = magic_levels[0]
    sum_of_both = current_material + current_magic

    check_the_sum(sum_of_both, gifts_to_craft, materials, magic_levels)
    if sum_of_both < 100:
        if sum_of_both % 2 == 0:
            sum_of_both = (current_material * 2) + (current_magic * 3)
            check_the_sum(sum_of_both, gifts_to_craft, materials, magic_levels)
            if sum_of_both < 100:
                materials.pop()
                magic_levels.popleft()

        else:
            sum_of_both = (current_material * 2) + (current_magic * 2)
            check_the_sum(sum_of_both, gifts_to_craft, materials, magic_levels)
            if sum_of_both < 100:
                materials.pop()
                magic_levels.popleft()

    if gifts_to_craft['Gemstone'] >= 1 and gifts_to_craft['Porcelain Sculpture'] >= 1 \
            or gifts_to_craft['Gold'] >= 1 and gifts_to_craft['Diamond Jewellery'] >= 1:
        is_win = True

if is_win:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")

if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")


for key, value in sorted(gifts_to_craft.items()):
    if value > 0:
        print(f"{key}: {value}")