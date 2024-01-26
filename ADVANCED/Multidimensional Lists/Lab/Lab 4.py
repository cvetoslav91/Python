rows, columns = [int(x) for x in input().split(', ')]
results = [0 for y in range(columns)]
for i in range(rows):
    current_row = [int(x) for x in input().split()]
    for j in range(len(current_row)):
        results[j] += current_row[j]

print(*results, sep="\n")