rows = int(input())
matrix = []
for i in range(rows):
    current_row = [int(x) for x in input().split(', ')]
    matrix.append([x for x in current_row if x % 2 == 0])

print(matrix)