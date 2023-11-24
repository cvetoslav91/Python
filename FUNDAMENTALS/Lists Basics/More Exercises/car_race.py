list = input().split()
middle_index = len(list) // 2
first_car = list[:middle_index]
second_car = list[middle_index + 1:]
second_car.reverse()
first_time = 0
second_time = 0
for time in first_car:
    if time == '0':
        first_time *= 0.8
    first_time += int(time)
for time in second_car:
    if time == '0':
        second_time *= 0.8
    second_time += int(time)
if first_time < second_time:
    print(f"The winner is left with total time: {first_time:.1f}")
else:
    print(f'The winner is right with total time: {second_time:.1f}')