def check_if_possible_move(row, col):
    if 0 <= row < rows and 0 <= col < columns:
        return True
    return False


def check_new_position():
    if field[row][col] == '*':
        return False
    return True


rows, columns = [int(x) for x in input().split()]
field = []

for i in range(rows):
    current_row = list(input())
    if 'B' in current_row:
        row = i
        col = current_row.index('B')
    field.append(current_row)

start_row = row
start_col = col

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()
while True:
    row = row + directions[command][0]
    col = col + directions[command][1]
    if check_if_possible_move(row, col):
        if check_new_position():
            new_symbol = field[row][col]
            field[row][col] = '.' if field[row][col] != 'R' else field[row][col]
            if new_symbol == 'P':
                field[row][col] = 'R'
                print('Pizza is collected. 10 minutes for delivery.')
            if new_symbol == 'A':
                field[row][col] = 'P'
                field[start_row][start_col] = 'B'
                print("Pizza is delivered on time! Next order...")
                [print(''.join(row)) for row in field]
                exit()
        else:
            row = row - directions[command][0]
            col = col - directions[command][1]

    else:
        field[start_row][start_col] = ' '
        print("The delivery is late. Order is canceled.")
        [print(''.join(row)) for row in field]
        exit()

    command = input()
