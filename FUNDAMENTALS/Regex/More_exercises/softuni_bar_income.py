import re

pattern = r'%([A-Z][a-z]+)%[^\|\.\$\%]*<(\w+)>[^\|\.\$\%]*\|(\d+)\|[^\|\.\$\%0-9]*(\d+\.?\d*)\$'
total_income = 0
while True:
    command = input()
    if command == 'end of shift':
        break
    result = re.findall(pattern, command)
    if result:
        for current in result:
            name = current[0]
            product = current[1]
            quantity = int(current[2])
            price = float(current[3])
            current_income = quantity * price
            total_income += current_income
            print(f'{name}: {product} - {current_income:.2f}')
print(f'Total income: {total_income:.2f}')