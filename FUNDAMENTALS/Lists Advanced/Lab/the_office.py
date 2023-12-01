happiness = list(map(int, input().split()))
factor = int(input())
new_happiness = [x * factor for x in happiness]
average = sum(new_happiness) / len(new_happiness)
happy_ppls = [x for x in new_happiness if x > average]
print(f'Score: {len(happy_ppls)}/{len(new_happiness)}.', end = " ")
if len(happy_ppls) * 2 >= len(new_happiness):
    print('Employees are happy!')
else:
    print('Employees are not happy!')