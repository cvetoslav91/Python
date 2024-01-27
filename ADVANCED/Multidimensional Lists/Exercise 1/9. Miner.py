squares = int(input())
commands = [x for x in input().split()]
commands = commands[-1::-1]
total_coals = 0
start_coord = []
maze = []
for i in range(squares):
    new_row = [x for x in input().split()]
    maze.append(new_row)
    if 's' in new_row:
        start_coord.append(i)
        start_coord.append(new_row.index('s'))
    if 'c' in new_row:
        count_coals = new_row.count('c')
        total_coals += count_coals
exit = False
all_coals_collected = False
current_row = start_coord[0]
current_col = start_coord[1]
coals_collected = 0
while commands:
    command = commands.pop()
    if command == 'up':
        if current_row - 1 >= 0:
            element_to_del = maze[current_row - 1][current_col]
            maze[current_row][current_col], maze[current_row - 1][current_col] = '*', \
                maze[current_row][current_col]
            new_position = [current_row - 1, current_col]
        else:
            continue

    elif command == 'down':
        if current_row + 1 < squares:
            element_to_del = maze[current_row + 1][current_col]
            maze[current_row][current_col], maze[current_row + 1][current_col] = '*', \
                maze[current_row][current_col]
            new_position = [current_row + 1, current_col]
        else:
            continue

    elif command == 'right':
        if current_col + 1 < squares:
            element_to_del = maze[current_row][current_col + 1]
            maze[current_row][current_col], maze[current_row][current_col + 1] = '*', \
                maze[current_row][current_col]
            new_position = [current_row , current_col + 1]
        else:
            continue

    elif command == 'left':
        if current_col - 1 >= 0:
            element_to_del = maze[current_row][current_col - 1]
            maze[current_row][current_col], maze[current_row][current_col - 1] = '*', \
                maze[current_row][current_col]
            new_position = [current_row , current_col - 1]
        else:
            continue

    current_row = new_position[0]
    current_col = new_position[1]
    if element_to_del == 'e':
        exit = True
        break
    elif element_to_del == 'c':
        coals_collected += 1
        if coals_collected == total_coals:
            all_coals_collected = True

if exit:
    print(f'Game over! ({current_row}, {current_col})')
elif all_coals_collected:
    print(f'You collected all coal! ({current_row}, {current_col})')
else:
    print(f'{total_coals - coals_collected} pieces of coal left. ({current_row}, {current_col})')