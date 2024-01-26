rows = int(input())
matrix = []
for i in range(rows):
    current_row = list(input())
    matrix.append(current_row)

symbol = input()

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == symbol:
            print(f'({i}, {j})')
            exit()
print(f'{symbol} does not occur in the matrix')