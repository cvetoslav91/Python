numbers = input().split()

moves = 0
while True:
    command = input()
    if command == 'end':
        print('Sorry you lose :(')
        print(*numbers)
        break
    moves += 1
    command = [int(s) for s in command.split()]
    first_index = command[0]
    second_index = command[1]
    if first_index < 0 or first_index > len(numbers) - 1 \
            or second_index < 0 or second_index > len(numbers) - 1 or first_index == second_index:
        index = (len(numbers) + 1) // 2
        numbers.insert(index, f"-{moves}a")
        numbers.insert(index, f"-{moves}a")
        print('Invalid input! Adding additional elements to the board')
    elif numbers[first_index] == numbers[second_index]:
        print(f"Congrats! You have found matching elements - {numbers[first_index]}!")
        if first_index < second_index:
            numbers.pop(second_index)
            numbers.pop(first_index)
        else:
            numbers.pop(first_index)
            numbers.pop(second_index)
    else:
        print("Try again!")
    if not numbers:
        print(f"You have won in {moves} turns!")
        break
