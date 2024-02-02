board_size = int(input())
field = []
for i in range(board_size):
    row_input = list(input())
    if 'G' in row_input:
        current_row = i
        current_col = row_input.index('G')
    field.append(row_input)

money = 100

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

command = input()

while command != 'end':
    field[current_row][current_col] = '-'
    current_row = current_row + directions[command][0]
    current_col = current_col + directions[command][1]
    if 0 <= current_row < board_size and 0 <= current_col < board_size:
        if field[current_row][current_col] == 'W':
            money += 100
            field[current_row][current_col] = '-'
        elif field[current_row][current_col] == 'P':
            money -= 200
            field[current_row][current_col] = '-'
            if money < 0:
                print('Game over! You lost everything!')
                exit()
        elif field[current_row][current_col] == 'J':
            money += 100000
            print('You win the Jackpot!')
            print(f'End of the game. Total amount: {money}$')
            field[current_row][current_col] = 'G'
            for x in field:
                print(''.join(x))
            exit()
    else:
        print('Game over! You lost everything!')
        exit()

    command = input()

field[current_row][current_col] = 'G'
print(f'End of the game. Total amount: {money}$')
for x in field:
    print(''.join(x))