budget_total = float(input())
statists = int(input())
price_dress_st = float(input())



if statists > 150:
    price_dress_st = price_dress_st - (price_dress_st * 0.1)

total_budget_for_statists = statists * price_dress_st
decor = budget_total * 0.1
all_costs = total_budget_for_statists + decor

if budget_total < all_costs:
    needed = all_costs - budget_total
    print("Not enough money!")
    print(f"Wingard needs {needed:.2f} leva more.")
else:
    over = budget_total - all_costs
    print("Action!")
    print(f"Wingard starts filming with {over:.2f} leva left.")