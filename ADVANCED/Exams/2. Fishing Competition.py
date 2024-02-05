square = int(input())
sea = []

for row in range(square):
    curr_row = list(input())
    if 'S' in curr_row:
        current_row = row
        current_col = curr_row.index('S')
    sea.append(curr_row)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

command = input()
collected_fish = 0
sea[current_row][current_col] = '-'

while command != 'collect the nets':
    current_row = current_row + directions[command][0]
    current_col = current_col + directions[command][1]
    if current_row < 0:
        current_row = square - 1
    if current_row == square:
        current_row = 0
    if current_col < 0:
        current_col = square - 1
    if current_col == square:
        current_col = 0
    if sea[current_row][current_col] == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{current_row},{current_col}]")
        exit()
    elif sea[current_row][current_col].isdigit():
        collected_fish += int(sea[current_row][current_col])
        sea[current_row][current_col] = '-'

    command = input()

else:
    sea[current_row][current_col] = 'S'
    if collected_fish < 20:
        diff = 20 - collected_fish
        print(f"You didn't catch enough fish and didn't reach the quota! You need {diff} tons of fish more.")
    elif collected_fish >= 20:
        print("Success! You managed to reach the quota!")
    if collected_fish > 0:
        print(f'Amount of fish caught: {collected_fish} tons.')
    for i in sea:
        print(''.join(i))
