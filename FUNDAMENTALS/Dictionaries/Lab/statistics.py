products_dictionary = {}
while True:
    product = input().split()
    if product[0] == 'statistics':
        break
    key = product[0]
    value = product[1]

    if key in products_dictionary:
        products_dictionary[key] += int(value)
    else:
        products_dictionary[key] = int(value)

print("Products in stock:")
for key, value in products_dictionary.items():
    print(f'- {key} {value}')
print(f'Total Products: {len(products_dictionary.keys())}')
print(f'Total Quantity: {sum(products_dictionary.values())}')