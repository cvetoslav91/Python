import re

bought = []
total_money = 0
pattern = r'>>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)'
while True:
    command = input()
    if command == 'Purchase':
        break
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought.append(furniture)
        total_money += float(price) * int(quantity)

print('Bought furniture:')
for current_furniture in bought:
    print(current_furniture)
print(f'Total money spend: {total_money:.2f}')