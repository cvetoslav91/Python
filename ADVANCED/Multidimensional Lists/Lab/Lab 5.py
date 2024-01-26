rows = int(input())
total_sum = 0
for i in range(rows):
    current_row = [int(x) for x in input().split()]
    total_sum += current_row[i]

print(total_sum)