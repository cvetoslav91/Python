numbers = [int(x) for x in input().split()]
while True:
    command = input().split()
    if command[0] == 'end':
        print(', '.join(map(str, numbers)))
        break
    if command[0] == 'swap':
        first_index = int(command[1])
        second_index = int(command[2])
        numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]
    if command[0] == 'multiply':
        first_index = int(command[1])
        second_index = int(command[2])
        numbers[first_index] *= numbers[second_index]
    if command[0] == 'decrease':
        numbers = [x - 1 for x in numbers]
