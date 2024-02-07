from collections import deque
from copy import deepcopy

def check_dots(row, col, field):
    coordinates = deque([[row, col]])
    counter = 1

    while coordinates:
        current_info = coordinates.popleft()
        current_row = current_info[0]
        current_col = current_info[1]

        field[current_row][current_col] = 'V'

        if current_row > 0:
            if field[current_row - 1][current_col] == '.':
                field[current_row - 1][current_col] = 'V'
                coordinates.append([current_row - 1, current_col])
                counter += 1

        if current_row < len(field) - 1:
            if field[current_row + 1][current_col] == '.':
                field[current_row + 1][current_col] = 'V'
                coordinates.append([current_row + 1, current_col])
                counter += 1

        if current_col > 0:
            if field[current_row][current_col - 1] == '.':
                field[current_row][current_col - 1] = 'V'
                coordinates.append([current_row, current_col - 1])
                counter += 1

        if current_col < len(field[0]) - 1:
            if field[current_row][current_col + 1] == '.':
                field[current_row][current_col + 1] = 'V'
                coordinates.append([current_row, current_col + 1])
                counter += 1

    return counter



field = []

n = int(input())
for i in range(n):
    r = [x for x in input().split()]
    field.append(r)

max_count = 0

for k in range(n):
    for j in range(len(field[0])):
        if field[k][j] == '.':
            current_count = check_dots(k, j, field)
            if current_count > max_count:
                max_count = current_count

print(max_count)


