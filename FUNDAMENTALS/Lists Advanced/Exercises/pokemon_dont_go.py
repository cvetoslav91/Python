distance = list(map(int, input().split())) # 5 10 6 3 5
new_list = []
final_sum = 0
while len(distance) != 0:
    index = int(input())
    if index < 0:
        index = 0
        poped_number = distance.pop(0)
        distance.insert(0, distance[-1])
        if len(distance) > 1:
            distance.insert(0, poped_number)
    elif index > len(distance) - 1:
        index = len(distance)
        poped_number = distance.pop(-1)
        distance.append(distance[0])
        if len(distance) > 1:
            distance.append(poped_number)
    number = distance.pop(index)
    final_sum += number
    for digit in distance:
        if digit <= number:
            digit += number
        else:
            digit -= number
        new_list.append(digit)
    if len(distance) == 0:
        break
    distance = new_list
    new_list = []
print(final_sum)
