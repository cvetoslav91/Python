import re

def sort_dict(dict):
    return dict[1][0], len(dict[1][1])


squares = int(input())
matrix = []
for row in range(squares):
    # current_row = [int(x) if re.findall(r'-?\d', x) else x for x in input().split()]
    current_row = input().split()
    matrix.append(current_row)
    if 'B' in current_row:
        b_row = row
        b_col = current_row.index('B')
start_row = b_row
start_col = b_col
directions = {
    'up': [0, []],
    'down': [0, []],
    'right': [0, []],
    'left': [0, []]
}
up_path = []
down_path = []
left_path = []
right_path = []

while b_row > 0:
    if matrix[b_row - 1][b_col] == 'X':
        break
    directions['up'][0] += int(matrix[b_row - 1][b_col])
    directions['up'][1].append([b_row - 1, b_col])
    b_row -= 1

b_row = start_row

while b_row < squares - 1:
    if matrix[b_row + 1][b_col] == 'X':
        break
    directions['down'][0] += int(matrix[b_row + 1][b_col])
    directions['down'][1].append([b_row + 1, b_col])
    b_row += 1

b_row = start_row

while b_col > 0:
    if matrix[b_row][b_col - 1] == 'X':
        break
    directions['left'][0] += int(matrix[b_row][b_col - 1])
    directions['left'][1].append([b_row, b_col - 1])
    b_col -= 1

b_col = start_col

while b_col < squares - 1:
    if matrix[b_row][b_col + 1] == 'X':
        break
    directions['right'][0] += int(matrix[b_row][b_col + 1])
    directions['right'][1].append([b_row, b_col + 1])
    b_col += 1
max_value = -1
for key, value in directions.items():
        if value[0] > max_value and len(value[1]) != 0:
            max_value = value[0]
            max_pos = key

print(max_pos)
for i in directions[max_pos][1]:
    print(i)
print(max_value)