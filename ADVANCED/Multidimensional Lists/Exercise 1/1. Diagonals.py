rows = int(input())
last_index = -1
primary_diagonal = []
secondary_diagonal = []
for i in range(rows):
    current_row = [int(x) for x in input().split(', ')]
    primary_diagonal.append(current_row[i])
    secondary_diagonal.append(current_row[last_index])
    last_index -= 1

primary_diagonal_f = ', '.join(map(str, primary_diagonal))
secondary_diagonal_f = ', '.join(map(str, secondary_diagonal))
print(f'Primary diagonal: {primary_diagonal_f}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {secondary_diagonal_f}. Sum: {sum(secondary_diagonal)}')
