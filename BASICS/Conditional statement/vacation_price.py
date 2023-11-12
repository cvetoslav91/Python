price_vacation = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_toys = puzzles + dolls + bears + minions + trucks

puzzles_income = puzzles * 2.6
dolls_income = dolls * 3
bears_income = bears * 4.1
minions_income = minions * 8.2
trucks_income = trucks * 2


all_income = puzzles_income + dolls_income + bears_income + minions_income + trucks_income

if total_toys >= 50:
    all_income = all_income - (all_income * 0.25)

all_income = all_income - (all_income * 0.1)

if price_vacation <= all_income:
    money_left = all_income - price_vacation
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_needed = price_vacation - all_income
    print(f'Not enough money! {money_needed:.2f} lv needed.')