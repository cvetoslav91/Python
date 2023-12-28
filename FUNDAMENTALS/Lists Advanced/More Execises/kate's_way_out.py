import copy
def move_up(kate_row, upper_row):
    index = kate_row.index("k")
    while upper_row[index] != ' ':
        kate_row[index], upper_row[index] = upper_row[index], kate_row[index]
        return upper_row, kate_row


def move_right(kate_row):
    index = kate_row.index('k')
    while kate_row[index + 1] != ' ':
        kate_row[index], kate_row[index + 1] = kate_row[index + 1], kate_row[index]
        return kate_row


def move_down(kate_row, under_row):
    index = kate_row.index("k")
    while under_row[index] != " ":
        kate_row[index], under_row[index] = under_row[index], kate_row[index]
        return under_row, kate_row

def move_left(kate_row):
    index = kate_row.index('k')
    moves = 0
    while kate_row[index - 1] != ' ':
        kate_row[index], kate_row[index - 1] = kate_row[index - 1], kate_row[index]
        moves += 1
        return kate_row


rows = int(input())
final_list = []
for current_row in range(1, rows + 1):
    new_row = input()
    row_list = [x for x in new_row]
    final_list.append(row_list)
    if 'k' in new_row:
        kate_row = current_row - 1

empty_squares = [final_list[x][y] for x in final_list for y in x if x == ' ']
print(empty_squares)