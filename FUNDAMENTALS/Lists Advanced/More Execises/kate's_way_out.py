def can_move(cur_row, cur_col, lab):
    if 0 <= cur_row < len(lab[0]) and 0 <= cur_col < len(lab[0]):
        return True
    return False

def check_free_spaces(cur_row, cur_col, lab, free = []):
    if cur_row - 1 >= 0:
        if lab[cur_row - 1][cur_col] == ' ':
            free.append('up')
    if cur_row + 1 < len(lab):
        if lab[cur_row + 1][cur_col] == ' ':
            free.append('down')
    if cur_col - 1 >= 0:
        if lab[cur_row][cur_col - 1] == ' ':
            free.append('left')
    if cur_col + 1 < len(lab[0]):
        if lab[cur_row][cur_col + 1] == ' ':
            free.append('right')
    return free

def check_if_trapped(cur_row, cur_col, lab):
    if cur_row - 1 >= 0 and cur_col - 1 >= 0 and cur_row + 1 < len(lab) and cur_col + 1 < len(lab[0]):
        return True
    return False


rows = int(input())
labyrinth = []
for row in range(rows):
    current_row = list(input())
    labyrinth.append(current_row)
    if 'k' in current_row:
        index = current_row.index('k')
        kates_position = [row, index]
current_row = kates_position[0]
current_col = kates_position[1]
moves = 0
moves_dict = {
    'up': [-1, 0],
    'left': [0, -1],
    'right': [0, 1],
    'down': [1, 0]
}
while kates_position:
    current_row = kates_position.pop(0)
    current_col = kates_position.pop(0)
    if can_move(current_row, current_col, labyrinth):
        free_spaces = check_free_spaces(current_row, current_col, labyrinth)
        if free_spaces:
            for current_free_space in free_spaces:
                labyrinth[current_row + moves_dict[current_free_space][0]][current_col + moves_dict[current_free_space][1]] = 'k'
            labyrinth[current_row][current_col] = '#'
            free_spaces.clear()
            moves += 1
            for r in range(len(labyrinth)):
                for c in range(len(labyrinth[0])):
                    if labyrinth[r][c] == 'k':
                        kates_position.append(r)
                        kates_position.append(c)
        else:
            if check_if_trapped(current_row, current_col, labyrinth):
                if kates_position:
                    continue
                else:
                    print('Kate cannot get out')
            else:
                print(f'Kate got out in {moves + 1} moves')

    else:
        if not kates_position:
            print('Kate cannot get out')
