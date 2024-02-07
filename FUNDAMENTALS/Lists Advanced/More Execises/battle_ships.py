n = int(input())
field = []

for row in range(n):
    curr_row = [int(x) for x in input().split()]
    field.append(curr_row)

attacks = [x for x in input().split()]
counter = 0

for current_attack in attacks:
    row, col = [int(x) for x in current_attack.split('-')]
    if field[row][col] > 0:
        field[row][col] -= 1
        if field[row][col] == 0:
            counter += 1

print(counter)