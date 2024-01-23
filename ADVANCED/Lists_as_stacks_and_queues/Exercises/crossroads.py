from collections import deque

green_light_time = int(input())
free_time = int(input())

cars = deque()
passed = 0
while True:
    command = input()

    if command == 'END':
        break

    if command == 'green':
        current_free_time = green_light_time
        while current_free_time > 0:
            if cars:
                car = cars.popleft()
            else:
                break
            for i in range(len(car)):
                current_free_time -= 1
                if current_free_time == 0:
                    cars.appendleft(car[i + 1:])
                    break
            else:
                passed += 1
        else:
            left_inside = cars.popleft()
            if len(left_inside) > free_time:
                hit_at = left_inside[free_time]
                print('A crash happened!')
                print(f'{car} was hit at {hit_at}.')
                exit()
            else:
                passed += 1

    else:
        cars.append(command)

print('Everyone is safe.')
print(f'{passed} total cars passed the crossroads.')