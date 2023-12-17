stock = input().split()
stock_dictionary = {}

for i in range(0, len(stock), 2):
    key = stock[i]
    value = stock[i + 1]
    stock_dictionary[key] = int(value)

searched_products = input().split()
for current_product in searched_products:
    if current_product in stock_dictionary:
        print(f"We have {stock_dictionary[current_product]} of {current_product} left")
    else:
        print(f"Sorry, we don't have {current_product}")