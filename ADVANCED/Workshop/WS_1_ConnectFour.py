def print_the_board(board):
    return '\n'.join(map(str, board))

def check_behind(row, col, field):
    number = field[row][col]
    repeats = 0
    while col > 0:
        if field[row][col - 1] == number:
            repeats += 1
            col -= 1
        else:
            break
    return repeats

def check_forward(row, col, field):
    number = field[row][col]
    repeats = 0
    while col < 6:
        if field[row][col + 1] == number:
            repeats += 1
            col += 1
        else:
            break
    return repeats

def check_horizontal(row, col, field):
    behind = check_behind(row, col, field)
    forward = check_forward(row, col, field)
    total = 1 + behind + forward
    return total

def check_down(row, col, field):
    number = field[row][col]
    repeats = 1
    while row < 5:
        if field[row + 1][col] == number:
            repeats += 1
            row += 1
        else:
            break
    return repeats

def check_left(row, col, field):
    number = field[row][col]
    repeats = 0
    while col > 0 and row > 0:
        if field[row - 1][col - 1] == number:
            repeats += 1
            row -= 1
            col -= 1
        else:
            break
    return repeats

def check_right(row, col, field):
    number = field[row][col]
    repeats = 0
    while col < 6 and row < 5:
        if field[row + 1][col + 1] == number:
            repeats += 1
            row += 1
            col += 1
        else:
            break
    return repeats


def check_main_diagonal(row, col, field):
    main = check_left(row, col, field)
    sec = check_right(row, col, field)
    total = 1 + main + sec
    return total

def check_back(row, col, board):
    number = board[row][col]
    repeats = 0
    while row < 5 and col > 0:
        if board[row + 1][col - 1] == number:
            repeats += 1
            row += 1
            col -= 1
        else:
            break
    return repeats

def check_front(row, col, board):
    number = board[row][col]
    repeats = 0
    while row > 0 and col < 6:
        if board[row - 1][col + 1] == number:
            repeats += 1
            row -= 1
            col += 1
        else:
            break
    return repeats


def check_secondary_diagonal(row, col, board):
    behind = check_back(row, col, board)
    forward = check_front(row, col, board)
    total = 1 + behind + forward
    return total


board = [[0 for _ in range(7)] for y in range(6)]
print(print_the_board(board))
turn = 1

for i in range(42):
    if turn % 2 == 1:
        column = int(input('Player 1, please choose a column: '))
        player = 1
    else:
        column = int(input('Player 2, please choose a column: '))
        player = 2

    for index in range(len(board) - 1, -1, -1):
        if column <= 0 or column > 7:
            print('Please enter valid column')
            break
        elif board[index][column - 1] == 0:
            board[index][column - 1] = player
            turn += 1
            if turn == 42:
                print('Draw')
                exit()
            break
    else:
        print('The column is full')
        continue

    if check_horizontal(index, column - 1, board) == 4 \
            or check_down(index, column - 1, board) == 4 \
            or check_main_diagonal(index, column - 1, board) == 4 \
            or check_secondary_diagonal(index, column - 1, board) == 4:
        print(f'Player {player} wins')
        print(print_the_board(board))
        exit()

    print(print_the_board(board))

