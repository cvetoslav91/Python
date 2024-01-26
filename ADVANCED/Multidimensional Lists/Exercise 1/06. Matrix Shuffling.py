rows, col = [int(x) for x in input().split()]
matrix = []
for i in range(rows):
    current_row = [x for x in input().split()]
    matrix.append(current_row)

command = input()
while command != 'END':
    info, *data = command.split()
    if info != 'swap' or len(data) != 4:
        print('Invalid input!')
        command = input()
        continue
    row1, col1, row2, col2 = [int(x) for x in data]
    if row1 < rows and row2 < rows and col1 < col and col2 < col:
        matrix[row1][col1],  matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for j in matrix:
            print(*j)
    else:
        print('Invalid input!')
    command = input()