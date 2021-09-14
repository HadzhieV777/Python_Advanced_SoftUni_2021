# 5. Truck Tour

from collections import deque

n = int(input())

gas_stations = deque()
for _ in range(n):
    gas_stations.append(input())


for big_circle_iteration in range(n):
    is_valid = True

    petrol_sum = 0
    for small_circle_iteration in range(n):
        current_station = gas_stations[small_circle_iteration]

        petrol, dstance_to_next_station = int(current_station.split()[0]), int(current_station.split()[1])
        petrol_sum += petrol - dstance_to_next_station

        if petrol_sum < 0:
            is_valid = False
            gas_stations.append(gas_stations.popleft())
            break

    if is_valid:
        print(big_circle_iteration)
        break