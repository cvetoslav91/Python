field = []
total_targets = 0
for i in range(5):
    row = input().split()
    if 'A' in row:
        current_row = i
        current_col = row.index('A')
    if 'x' in row:
        total_targets += row.count('x')
    field.append(row)

targets_shot = 0
targets = []

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'move':
        if command[1] == 'right':
            if current_col + int(command[2]) < 5:
                if field[current_row][current_col + int(command[2])] == '.':
                    field[current_row][current_col] = '.'
                    field[current_row][current_col + int(command[2])] = 'A'
        elif command[1] == 'left':
            if current_col - int(command[2]) >= 0:
                if field[current_row][current_col - int(command[2])] == '.':
                    field[current_row][current_col] = '.'
                    field[current_row][current_col - int(command[2])] = 'A'
        elif command[1] == 'up':
            if current_row - int(command[2]) >= 0:
                if field[current_row - int(command[2])][current_col] == '.':
                    field[current_row][current_col] = '.'
                    field[current_row - int(command[2])][current_col] = 'A'
        elif command[1] == 'down':
            if current_row + int(command[2]) < 5:
                if field[current_row + int(command[2])][current_col] == '.':
                    field[current_row][current_col] = '.'
                    field[current_row + int(command[2])][current_col] = 'A'

    elif command[0] == 'shoot':
        if command[1] == 'right':
            for i in range(current_col + 1, 5):
                if field[current_row][i] == 'x':
                    field[current_row][i] = '.'
                    targets_shot += 1
                    targets.append([current_row, i])
                    break
        elif command[1] == 'left':
            for i in range(current_col - 1, -1, -1):
                if field[current_row][i] == 'x':
                    field[current_row][i] = '.'
                    targets_shot += 1
                    targets.append([current_row, i])
                    break
        elif command[1] == 'up':
            for i in range(current_row - 1, -1, -1):
                if field[i][current_col] == 'x':
                    field[i][current_col] = '.'
                    targets_shot += 1
                    targets.append([i, current_col])
                    break
        elif command[1] == 'down':
            for i in range(current_row + 1, 5):
                if field[i][current_col] == 'x':
                    field[i][current_col] = '.'
                    targets_shot += 1
                    targets.append([i, current_col])
                    break
    if targets_shot == total_targets:
        print(f"Training completed! All {total_targets} targets hit.")
        print(*targets, sep='\n')
        exit()
    for i in range(5):
        for j in range(5):
            if field[i][j] == 'A':
                current_row = i
                current_col = j

else:
    print(f"Training not completed! {total_targets - targets_shot} targets left.")
    print(*targets, sep='\n')