# 04. Parking Lot
parking = set()

n = int(input())
IN_CMD = "IN"
OUT_CMD = "OUT"

for _ in range(n):
    commands = input().split(", ")
    command = commands[0]
    car_number = commands[1]

    if command == IN_CMD:
        parking.add(car_number)
    elif command == OUT_CMD:
        if car_number in parking:
            parking.remove(car_number)

if parking:
    for car_num in parking:
        print(car_num)
else:
    print('Parking Lot is Empty')