rows = int(input())
last_index = -1
primary_diagonal = []
secondary_diagonal = []
for i in range(rows):
    current_row = [int(x) for x in input().split()]
    primary_diagonal.append(current_row[i])
    secondary_diagonal.append(current_row[last_index])
    last_index -= 1

difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(difference)