rows = int(input())
matrix = []
for i in range(rows):
    current_row = [int(x) for x in input().split(', ')]
    for j in current_row:
        matrix.append(j)

print(matrix)