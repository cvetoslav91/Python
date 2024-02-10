from collections import deque

def check_win():

    win_row = any([all(el == players[0][1] for el in row) for row in board])
    win_col = any([all(board[r][col] == players[0][1] for r in range(size))for col in range(size)])
    win_main_diagonal = all([board[i][i] == players[0][1] for i in range(size)])
    secondary_diagonal = all([board[sec][size - 1 - sec] == players[0][1] for sec in range(size)])
    if any([win_row, win_col, win_main_diagonal, secondary_diagonal]):
        return True
def play():
    global turns
    while True:
        try:
            position = int(input(f'{players[0][0]} please select a position: '))
            row = (position - 1) // size
            col = (position - 1) % size
        except ValueError:
            print('Please select a valid position: ')
            continue

        if 0 < position <= size * size and board[row][col] == ' ':
            turns += 1
            board[row][col] = players[0][1]
            break

    if turns > 4:
        win = check_win()
        if win:
            print_board()
            print(f'{players[0][0]} win')
            exit()
    print_board()

    if turns == 9:
        print('Draw')
        exit()

    players.rotate()
    play()

def print_board():
    for row in range(size):
        print(f"| {' | '.join(board[row])} |")


def board_start():
    print_board()
    for x in range(len(board)):
        for y in range(len(board)):
            board[x][y] = ' '

    play()

player_one = input('Player 1, Enter Your Name: ')
player_two = input('Player 2, Enter Your Name: ')

while True:
    player_one_symbol = input(f'{player_one}, please select your symbol: X or O: ').upper()
    if player_one_symbol == 'X' or player_one_symbol == 'O':
        break
    else:
        print('Please enter a valid symbol')

player_two_symbol = 'X' if player_one_symbol == 'O' else 'O'
players = deque()
players.append([player_one, player_one_symbol])
players.append([player_two, player_two_symbol])

turns = 0
size = 3
board = ([[str(y) for y in range(row, row + size)] for row in range(1, size * size + 1, size)])
board_start()
