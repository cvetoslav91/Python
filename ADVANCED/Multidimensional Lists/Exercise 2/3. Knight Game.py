def back_long(row, col, matrix):
    if row - 2 >= 0 and col - 1 >= 0:
        return matrix[row - 2][col - 1]
    return False
def back_long_right(row, col, matrix):
    if row - 2  >= 0 and col + 1 < len(matrix):
        return matrix[row - 2][col + 1]
    return False

def back_short(row, col, matrix):
    if row - 1 >= 0 and col - 2 >= 0:
        return matrix[row - 1][col - 2]
    return False

def back_short_right(row, col, matrix):
    if row - 1 >= 0 and col + 2 < len(matrix):
        return matrix[row - 1][col + 2]
    return False

def forward_short(row, col, matrix):
    if row + 1 < len(matrix) and col - 2 >= 0:
        return matrix[row + 1][col - 2]
    return False

def forward_short_right(row, col, matrix):
    if row + 1 < len(matrix) and col + 2 < len(matrix):
        return matrix[row + 1][col + 2]
    return False

def forward_long(row, col, matrix):
    if row + 2 < len(matrix) and col - 1 >= 0:
        return matrix[row + 2][col - 1]
    return False

def forward_long_right(row, col, matrix):
    if row + 2 < len(matrix) and col + 1 < len(matrix):
        return matrix[row + 2][col + 1]
    return False




squares = int(input())

board = []
for _ in range(squares):
    curr_row = list(input())
    board.append(curr_row)
max_taken = 0
knights_removed = 0
while True:
    for current_row in range(squares):
        for current_square in range(squares):
            if board[current_row][current_square] == 'K':
                taken = 0
                if back_short(current_row, current_square, board) == 'K':
                    taken += 1
                if back_long(current_row, current_square, board) == 'K':
                    taken += 1
                if back_long_right(current_row, current_square, board) == 'K':
                    taken += 1
                if back_short_right(current_row, current_square, board) == 'K':
                    taken += 1
                if forward_long(current_row, current_square, board) == 'K':
                    taken += 1
                if forward_short(current_row, current_square, board) == 'K':
                    taken += 1
                if forward_short_right(current_row, current_square, board) == 'K':
                    taken += 1
                if forward_long_right(current_row, current_square, board) == 'K':
                    taken += 1
                if taken > max_taken:
                    max_taken = taken
                    should_be_removed = [current_row, current_square]
    if max_taken == 0:
        print(knights_removed)
        exit()
    board[should_be_removed[0]][should_be_removed[1]] = 0
    knights_removed += 1
    max_taken = 0
