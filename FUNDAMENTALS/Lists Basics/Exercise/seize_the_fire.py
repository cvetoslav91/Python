fires = input().split('#')
water = int(input())
total_fire = 0
cells = []
for i in range(len(fires)):
    current_fire = fires[i]
    curr_fire_separate = current_fire.split(' = ')
    type_of_fire = curr_fire_separate[0]
    strenght_of_fire = int(curr_fire_separate[1])
    if (type_of_fire == 'Low' and 1 <= strenght_of_fire <= 50) \
        or (type_of_fire == 'Medium' and 51 <= strenght_of_fire <= 80) \
        or (type_of_fire == 'High' and 81 <= strenght_of_fire <= 125):
        if strenght_of_fire > water:
            continue
        else:
            water -= strenght_of_fire
            total_fire += strenght_of_fire
            cells.append(strenght_of_fire)
print('Cells:')
for j in cells:
    print(f' - {j}')
efforts = total_fire * 0.25
print(f'Effort: {efforts:.2f}')
print(f'Total Fire: {total_fire}')

