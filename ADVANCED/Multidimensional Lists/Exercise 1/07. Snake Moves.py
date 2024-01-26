rows, col = [int(x) for x in input().split()]
matrix = []
snake = input()
index_of_snake = 0
for row in range(rows):
    current_row = []
    for column in range(col):
        current_row.append(snake[0])
        snake = snake[1:] + snake[0]
    if row % 2 == 0:
        print(*current_row, sep='')
    else:
        print(*current_row[-1::-1], sep='')