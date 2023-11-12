budget = float(input())
excl = input()
fans = int(input())

vip_ticket = 499.99
normal_ticket = 249.99
transport = 0
tickets = 0
total_cost = 0
difference = 0
#1 до 4 – 75% от бюджета.
#•	От 5 до 9 – 60% от бюджета.
#•	От 10 до 24 – 50% от бюджета.
#•	От 25 до 49 – 40% от бюджета.
#•	50 или повече – 25% от бюджета.
money_left = 0
tickets_all = 0
difference = 0
if excl == 'VIP':
    if 1 <= fans <= 4:
        transport = budget * 0.75
        money_left = budget - transport
        tickets_all = fans * vip_ticket

    elif 5 <= fans <= 9:
        transport = budget * 0.6
        money_left = budget - transport
        tickets_all = fans * vip_ticket

    elif 10 <= fans <= 24:
        transport = budget * 0.5
        money_left = budget - transport
        tickets_all = fans * vip_ticket

    elif 25 <= fans <= 50:
        transport = budget * 0.4
        money_left = budget - transport
        tickets_all = fans * vip_ticket

    elif fans > 50:
        transport = budget * 0.25
        money_left = budget - transport
        tickets_all = fans * vip_ticket

elif excl == 'Normal':
    if 1 <= fans <= 4:
        transport = budget * 0.75
        money_left = budget - transport
        tickets_all = fans * normal_ticket

    elif 5 <= fans <= 9:
        transport = budget * 0.6
        money_left = budget - transport
        tickets_all = fans * normal_ticket

    elif 10 <= fans <= 24:
        transport = budget * 0.5
        money_left = budget - transport
        tickets_all = fans * normal_ticket

    elif 25 <= fans <= 50:
        transport = budget * 0.4
        money_left = budget - transport
        tickets_all = fans * normal_ticket

    elif fans > 50:
        transport = budget * 0.25
        money_left = budget - transport
        tickets_all = fans * normal_ticket

difference = abs(money_left - tickets_all)
if money_left >= tickets_all:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')