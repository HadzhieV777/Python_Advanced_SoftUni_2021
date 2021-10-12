# 01. Bombs

from collections import deque

bomb_effects, bomb_casings = deque([int(x) for x in input().split(", ")]), [int(x) for x in input().split(", ")]

datura_bombs_count, cherry_bombs_count, smoke_decoy_bombs_count = 0, 0, 0

while bomb_effects and bomb_casings:
    current_effect, current_casing = bomb_effects.popleft(), bomb_casings.pop()
    sum_of_both = current_effect + current_casing

    if sum_of_both == 40:
        datura_bombs_count += 1

    elif sum_of_both == 60:
        cherry_bombs_count += 1

    elif sum_of_both == 120:
        smoke_decoy_bombs_count += 1

    else:
        bomb_effects.appendleft(current_effect)
        bomb_casings.append(current_casing - 5)

    if datura_bombs_count >= 3 and cherry_bombs_count >= 3 and smoke_decoy_bombs_count >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        break

else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")


if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")


print(f"Cherry Bombs: {cherry_bombs_count}")
print(f"Datura Bombs: {datura_bombs_count}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs_count}")