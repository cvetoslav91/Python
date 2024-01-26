rows, col = [int(x) for x in input().split()]
matrix = []
counter = 0
for i in range(rows):
    current_row = [x for x in input().split()]
    matrix.append(current_row)

for row in range(rows - 1):
    for columns in range(col - 1):
        if matrix[row][columns] == matrix[row][columns + 1] \
            and matrix[row][columns] == matrix[row + 1][columns] \
            and matrix[row][columns] == matrix[row + 1][columns + 1]:
            counter += 1

print(counter)