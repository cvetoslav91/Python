clothes = [int(x) for x in input().split()]
capacity = int(input())
racks_needed = 0
free_space = capacity
for i in range(len(clothes)):
    number_of_clothes = clothes.pop()
    if number_of_clothes <= free_space:
        free_space -= number_of_clothes
        if free_space <= 0:
            racks_needed += 1
            free_space = capacity
    else:
        racks_needed += 1
        free_space = capacity
        free_space -= number_of_clothes
if racks_needed == 1:
    print(1)
else:
    print(racks_needed + 1)