rows, columns = [int(x) for x in input().split(', ')]
total_sum = 0
matrix = []
for i in range(rows):
    current_column = [int(x) for x in input().split(', ')]
    matrix.append(current_column)
    total_sum += sum(current_column)

print(total_sum)
print(matrix)