rows, cols = [int(x) for x in input().split()]

for row in range(rows):
    for col in range(cols):
        print(f'{chr(row + 97)}', end="")
        print(f'{chr(row + col + 97)}', end="")
        print(f'{chr(row + 97)}', end=' ')
    print()