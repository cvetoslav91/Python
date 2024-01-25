first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))
lines = int(input())
for _ in range(lines):
    command = input().split()
    numbers = [int(x) for x in command[2:]]
    if command[0] == 'Add':
        if command[1] == 'First':
            for number in numbers:
                first_sequence.add(number)
        elif command[1] == 'Second':
            for number in numbers:
                second_sequence.add(number)
    elif command[0] == 'Remove':
        if command[1] == 'First':
            for number in numbers:
                if number in first_sequence:
                    first_sequence.remove(number)
        elif command[1] == 'Second':
            for number in numbers:
                if number in second_sequence:
                    second_sequence.remove(number)
    elif command[0] == 'Check':
        if first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence):
            print('True')
        else:
            print('False')

first_sequence = list(sorted(first_sequence))
second_sequence = list(sorted(second_sequence))
print(*first_sequence, sep=', ')
print(*second_sequence, sep=', ')