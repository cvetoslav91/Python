from collections import deque

petrol_pumps = int(input())
litres = deque()
kms = deque()
smallest_start_index = 0
for i in range(petrol_pumps):
    litre, km = input().split()
    litres.append(litre)
    kms.append(km)


for index in range(len(litres)):
    fuel = 0
    not_possible = False
    for i in range(len(litres)):
        current_litres_filled = int(litres[i])
        distance_to_next_stop = int(kms[i])
        if fuel + current_litres_filled >= distance_to_next_stop:
            fuel += current_litres_filled - distance_to_next_stop
        else:
            not_possible = True
            break
    if not_possible:
        litres.rotate(-1)
        kms.rotate(-1)
    else:
        print(index)
        exit()