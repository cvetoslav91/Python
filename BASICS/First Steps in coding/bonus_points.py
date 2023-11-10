points = int(input())

# bonus points
# points + bonus points

# За четно число  + 1 т.
# За число, което завършва на 5  + 2 т.

if points <= 100:
    bonus = 5
    if (points % 2) == 0:
        bonus = bonus + 1
        sum_points = points + bonus
        print(bonus, end='\n')
        print(sum_points)
    elif points % 10 == 5:
        bonus = bonus + 2
        sum_points = points + bonus
        print(bonus, end='\n')
        print(sum_points)
elif 100 < points < 1000:
    if (points % 2) == 0:
        bonus = points * (20 / 100) + 1
        sum_points = points + bonus
        print(bonus, end='\n')
        print(sum_points)
    elif points % 10 == 5:
        bonus = points * (20 / 100) + 2
        sum_points = points + bonus
        print(bonus, end='\n')
        print(sum_points)
elif points > 1000:
    if (points % 2) == 0:
        bonus = (points * (10 / 100)) + 1
        sum_points = points + bonus
        print(bonus, end='\n')
        print(sum_points)
    elif points % 10 == 5:
        bonus = (points * (10 / 100)) + 2
        sum_points = points + bonus
        print(bonus, end='\n')
        print(sum_points)
