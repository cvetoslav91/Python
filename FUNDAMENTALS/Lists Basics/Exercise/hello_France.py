items = input().split('|')
budget = float(input())
train_ticket = 150
list_with_profits = []
total_profit = 0
new_budget = 0
for i in range(len(items)):
    current_item = items[i]
    separate_items = current_item.split('->')
    type_of_item = separate_items[0]
    value = float(separate_items[1])
    if value > budget:
        continue
    elif (type_of_item == 'Clothes' and value <= 50) or \
            (type_of_item == 'Shoes' and value <= 35) or \
            (type_of_item == 'Accessories' and value <= 20.50):
        budget -= value
        new_price = value * 1.4
        new_budget += new_price
        current_profit = new_price - value
        total_profit += current_profit
        list_with_profits.append(new_price)
for j in range(len(list_with_profits)):
    if j == len(list_with_profits) - 1:
        print(f'{list_with_profits[j]:.2f}')
    else:
        print(f'{list_with_profits[j]:.2f}', end=" ")
print(f'Profit: {total_profit:.2f}')
total_money = new_budget + budget
if total_money >= train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')