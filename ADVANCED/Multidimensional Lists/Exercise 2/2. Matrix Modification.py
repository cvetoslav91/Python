def check_indices(matrix, index_row, index_col):
    if 0 <= index_row < len(matrix) and 0 <= index_col < len(matrix[0]):
        return True
    return False

matrix = []

for i in range(int(input())):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)

command = input()
while command != 'END':
    com, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)
    if check_indices(matrix, row, col):
        if com == 'Add':
            matrix[row][col] += value
        elif com == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')
    command = input()

for r in matrix:
    print(*r)