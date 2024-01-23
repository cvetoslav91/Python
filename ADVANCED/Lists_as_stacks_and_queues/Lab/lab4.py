from collections import deque

water_quantity = int(input())
peoples = deque()

while True:
    command = input()
    if command == 'Start':
        break
    peoples.append(command)

while True:
    info = input().split()
    if info[0] == 'End':
        break
    elif info[0] == 'refill':
        water_quantity += int(info[1])
    elif len(info) == 1:
        person = peoples.popleft()
        if int(info[0]) > water_quantity:
            print(f"{person} must wait")
        else:
            print(f"{person} got water")
            water_quantity -= int(info[0])

print(f"{water_quantity} liters left")