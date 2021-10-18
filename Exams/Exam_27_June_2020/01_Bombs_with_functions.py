# 01. Bombs with functions
#
# from collections import deque
#
#
# def print_the_success(success):
#     if success:
#         print("Bene! You have successfully filled the bomb pouch!")
#     else:
#         print("You don't have enough materials to fill the bomb pouch.")
#
#
# def print_the_remaining_materials(bombs_dict, cassings_dict):
#     if bombs_dict:
#         print(f"Bomb Effects: {', '.join([str(x) for x in bombs_dict])}")
#     else:
#         print("Bomb Effects: empty")
#
#     if cassings_dict:
#         print(f"Bomb Casings: {', '.join([str(x) for x in cassings_dict])}")
#     else:
#         print("Bomb Casings: empty")
#
#
# def print_the_created_bombs(bombs):
#     print(f'''Cherry Bombs: {bombs["cherry_bombs"][1]}
# Datura Bombs: {bombs["datura_bombs"][1]}
# Smoke Decoy Bombs: {bombs["smoke_decoy_bombs"][1]}''')
#
#
# def create_a_bomb(effect, casing, bombs_dict):
#     if (current_effect + current_casing) == bombs["datura_bombs"][0]:
#         bombs["datura_bombs"][1] += 1
#     elif (current_effect + current_casing) == bombs["cherry_bombs"][0]:
#         bombs["cherry_bombs"][1] += 1
#     elif (current_effect + current_casing) == bombs["smoke_decoy_bombs"][0]:
#         bombs["smoke_decoy_bombs"][1] += 1
#
#
# bomb_effects = deque([int(x) for x in input().split(", ")])
# bomb_casings = [int(x) for x in input().split(", ")]
#
# bombs = {
#     "datura_bombs": [40, 0],
#     "cherry_bombs": [60, 0],
#     "smoke_decoy_bombs": [120, 0],
# }
#
#
# success = False
# while bomb_effects and bomb_casings:
#     current_effect = bomb_effects[0]
#     current_casing = bomb_casings[-1]
#
#     if (current_effect + current_casing) == bombs["datura_bombs"][0] or \
#         (current_effect + current_casing) == bombs["cherry_bombs"][0] or \
#             (current_effect + current_casing) == bombs["smoke_decoy_bombs"][0]:
#         bomb_effects.popleft()
#         bomb_casings.pop()
#
#         create_a_bomb(current_effect, current_casing, bombs)
#
#     else:
#         bomb_casings[-1] -= 5
#
#     if bombs["datura_bombs"][1] >= 3 and bombs["cherry_bombs"][1] >= 3 and bombs["smoke_decoy_bombs"][1] >= 3:
#         success = True
#         break
#
# print_the_success(success)
# print_the_remaining_materials(bomb_effects, bomb_casings)
# print_the_created_bombs(bombs)
