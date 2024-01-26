from math import inf

rows, col = [int(x) for x in input().split()]
matrix = []
for i in range(rows):
    current_row = [int(x) for x in input().split()]
    matrix.append(current_row)
max_sum = -inf
sub_matrixes = []
for row in range(rows - 2):
    for column in range(col - 2):
        current_el = matrix[row][column]
        next_el = matrix[row][column + 1]
        third_el = matrix[row][column + 2]
        under_el = matrix[row + 1][column]
        undernext_el = matrix[row + 1][column + 1]
        underthird_el = matrix[row + 1][column + 2]
        downunder_el = matrix[row + 2][column]
        dun_el = matrix[row + 2][column + 1]
        diagonal_el = matrix[row + 2][column + 2]

        sub1 = [current_el, next_el, third_el]
        sub2 = [under_el, undernext_el, underthird_el]
        sub3 = [downunder_el, dun_el, diagonal_el]
        total_sum = (sum(sub1) + sum(sub2) + sum(sub3))
        if total_sum > max_sum:
            max_sum = total_sum
            sub_matrixes = []
            sub_matrixes.append(sub1)
            sub_matrixes.append(sub2)
            sub_matrixes.append(sub3)

print(f"Sum = {max_sum}")
print(*sub_matrixes[0])
print(*sub_matrixes[1])
print(*sub_matrixes[2])