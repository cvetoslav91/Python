presents = int(input())
field = []
good_kids = 0
for i in range(int(input())):
    row = input().split()
    if 'S' in row:
        current_row = i
        current_col = row.index('S')
    if 'V' in row:
        good_kids += row.count('V')
    field.append(row)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
total_good_kids = good_kids
command = input()

while command != 'Christmas morning':
    new_symbol = field[current_row + directions[command][0]][current_col + directions[command][1]]
    field[current_row][current_col] = '-'
    current_row = current_row + directions[command][0]
    current_col = current_col + directions[command][1]
    field[current_row][current_col] = 'S'
    if new_symbol == 'V':
        presents -= 1
        good_kids -= 1
        if good_kids == 0:
            for i in field:
                print(*i)
            print(f'Good job, Santa! {total_good_kids} happy nice kid/s.')
            exit()
    elif new_symbol == 'C':
        if field[current_row - 1][current_col] == 'X' or field[current_row - 1][current_col] == 'V':
            field[current_row - 1][current_col] = '-'
            presents -= 1
        if field[current_row + 1][current_col] == 'X' or field[current_row + 1][current_col] == 'V':
            field[current_row + 1][current_col] = '-'
            presents -= 1
        if field[current_row][current_col - 1] == 'X' or field[current_row][current_col - 1] == 'V':
            field[current_row][current_col - 1] = '-'
            presents -= 1
        if field[current_row][current_col + 1] == 'X' or field[current_row][current_col + 1] == 'V':
            field[current_row][current_col + 1] = '-'
            presents -= 1

    good_kids = 0
    for i in field:
        if 'V' in i:
            good_kids += i.count('V')

    if good_kids == 0:
        for i in field:
            print(*i)
        print(f'Good job, Santa! {total_good_kids} happy nice kid/s.')
        exit()

    if presents <= 0:
        print(f'Santa ran out of presents!')
        for i in field:
            print(*i)
        print(f'No presents for {good_kids} nice kid/s.')
        exit()

    command = input()

for i in field:
    print(*i)
print(f'No presents for {good_kids} nice kid/s.')