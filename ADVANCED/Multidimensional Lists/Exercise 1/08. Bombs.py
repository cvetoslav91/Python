rows = int(input())
matrix = []
for i in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

bombs = [list(map(int, x.split(','))) for x in input().split()]

for coordinates in bombs:
    row1, col1 = coordinates
    number = matrix[row1][col1]
    if number <= 0:
        continue
    for h in range(row1 - 1 if row1 - 1 > 0 else 0, row1 + 2 if row1 + 1 < len(matrix) else len(matrix)):
        for k in range(col1 - 1 if col1 - 1 > 0 else 0, col1 + 2 if col1 + 1 < len(matrix) else len(matrix)):
            if h == row1 and k == col1:
                matrix[h][k] = 0
            else:
                if matrix[h][k] > 0:
                    matrix[h][k] -= number
alive_cells = 0
total_sum = 0
for row in range(rows):
    for column in range(rows):
        if matrix[row][column] > 0:
            total_sum += matrix[row][column]
            alive_cells += 1
print(f'Alive cells: {alive_cells}')
print(f'Sum: {total_sum}')
for i in matrix:
    print(*i)