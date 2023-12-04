queue = int(input())
wagons = [int(s) for s in input().split()]
for current_wagon in range(len(wagons)):
    current_peoples = wagons[current_wagon]
    free_places = 4 - wagons[current_wagon]
    if queue >= 4:
        wagons[current_wagon] = 4
        peoples_left = free_places
    else:
        wagons[current_wagon] = queue + current_peoples
        peoples_left = queue
    queue -= peoples_left
if queue == 0 and wagons[-1] != 4:
    print('The lift has empty spots!')
elif queue == 0 and wagons[-1] == 4:
    pass
else:
    print(f"There isn't enough space! {queue} people in a queue!")
print(*wagons)