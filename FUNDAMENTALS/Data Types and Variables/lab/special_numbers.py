n = int(input())

for i in range(1, n + 1):
    i = str(i)
    total = 0
    special_number = False
    for j in i:
        j = int(j)
        total += j
    if total == 5 or total == 7 or total == 11:
        special_number = True
    print(f'{i} -> {special_number}')

