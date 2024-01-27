def player_is_alive(lair):
    for i in range(len(lair)):
        for j in range(len(lair[0])):
            if lair[i][j] == 'P':
                return True
    return False

def spread_bunnies(lair):
    for i in range(len(lair)):
        for j in range(len(lair[0])):
            if lair[i][j] == 'B':
                if i > 0:
                    if lair[i - 1][j] == '.' or lair[i - 1][j] == 'P':
                        lair[i - 1][j] = 'b'
                if i < len(lair) - 1:
                    if lair[i + 1][j] == '.' or lair[i + 1][j] == 'P':
                        lair[i + 1][j] = 'b'
                if j > 0:
                    if lair[i][j - 1] == '.' or lair[i][j - 1] == 'P':
                        lair[i][j - 1] = 'b'
                if j < len(lair[0]) - 1:
                    if lair[i][j + 1] == '.' or lair[i][j + 1] == 'P':
                        lair[i][j + 1] = 'b'
    return lair


def can_move(direction, lair, cur_row, cur_col):
    new_row = commands_list[direction][0] + cur_row
    new_col = commands_list[direction][1] + cur_col
    if 0 <= new_row < len(lair) and 0 <= new_col < len(lair[0]):
        return True
    return False


from collections import deque
rows, columns = [int(x) for x in input().split()]
lair = []

for row in range(rows):
    current_column = list(input())
    if 'P' in current_column:
        row_of_player = row
        col_of_player = current_column.index('P')
    lair.append(current_column)



command = deque(list(input()))
commands_list = {
    'U': [-1, 0],
    'L': [0, -1],
    'R': [0, 1],
    'D': [1, 0]
}
won = False
dead = False
while command:
    new_command = command.popleft()
    if can_move(new_command, lair, row_of_player, col_of_player):
        if lair[row_of_player + commands_list[new_command][0]][col_of_player + commands_list[new_command][1]] == 'B':
            lair = spread_bunnies(lair)
            for i in range(len(lair)):
                for j in range(len(lair[0])):
                    if lair[i][j] == 'b':
                        lair[i][j] = 'B'
            row_of_player = row_of_player + commands_list[new_command][0]
            col_of_player = col_of_player + commands_list[new_command][1]
            for i in lair:
                print(''.join(i))
            print(f"dead: {row_of_player} {col_of_player}")
            exit()

        lair[row_of_player][col_of_player],  lair[row_of_player + commands_list[new_command][0]][col_of_player + commands_list[new_command][1]]\
            = lair[row_of_player + commands_list[new_command][0]][col_of_player + commands_list[new_command][1]], lair[row_of_player][col_of_player]
        row_of_player = row_of_player + commands_list[new_command][0]
        col_of_player = col_of_player + commands_list[new_command][1]
    else:
        lair = spread_bunnies(lair)
        for i in range(len(lair)):
            for j in range(len(lair[0])):
                if lair[i][j] == 'b':
                    lair[i][j] = 'B'
        for i in range(len(lair)):
            for j in range(len(lair[0])):
                if lair[i][j] == 'P':
                    lair[i][j] = '.'
        for i in lair:
            print(''.join(i))
        print(f"won: {row_of_player} {col_of_player}")
        exit()

    lair = spread_bunnies(lair)
    for i in range(len(lair)):
        for j in range(len(lair[0])):
            if lair[i][j] == 'b':
                lair[i][j] = 'B'

    if player_is_alive(lair):
        continue
    else:
        for i in lair:
            print(''.join(i))
        print(f"dead: {row_of_player} {col_of_player}")
        exit()