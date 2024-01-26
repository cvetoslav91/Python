from math import inf
rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for i in range(rows):
    current_row = [int(x) for x in input().split(', ')]
    matrix.append(current_row)

max_sum = -inf
final_matrix = []
for row in range(rows - 1):
    for column in range(columns - 1):
        current_el = matrix[row][column]
        next_el = matrix[row][column + 1]
        under_el = matrix[row + 1][column]
        diagonal_el = matrix[row + 1][column + 1]
        total_sum = current_el + next_el + under_el + diagonal_el
        if total_sum > max_sum:
            max_sum = total_sum
            final_matrix = [[current_el, next_el], [under_el, diagonal_el]]

print(*final_matrix[0])
print(*final_matrix[1])
print(max_sum)