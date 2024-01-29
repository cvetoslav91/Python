def next_square_is_inside(field, new_row, new_col):
    if 0 <= current_row + new_row < squares and 0 <= current_col + new_col < squares:
        return True
    return False

squares = int(input())
field = []
for i in range(squares):
    row = [x for x in input().split()]
    field.append(row)
    if 'A' in row:
        current_row = i
        current_col = row.index('A')
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
teas_collected = 0
while teas_collected < 10:
    command = input()
    if next_square_is_inside(field, directions[command][0], directions[command][1]):
        field[current_row][current_col] = '*'
        current_row = current_row + directions[command][0]
        current_col = current_col + directions[command][1]
        if field[current_row][current_col] == 'R':
            field[current_row][current_col] = '*'
            print("Alice didn't make it to the tea party.")
            for i in field:
                print(*i)
            exit()
        if field[current_row][current_col] == '.' or field[current_row][current_col] == '*':
            continue
        teas_collected += int(field[current_row][current_col])
    else:
        field[current_row][current_col] = '*'
        print("Alice didn't make it to the tea party.")
        for i in field:
            print(*i)
        exit()

field[current_row][current_col] = '*'
print("She did it! She went to the party.")
for i in field:
    print(*i)