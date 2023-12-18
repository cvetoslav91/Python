dictionary = {}
while True:
    command = input()
    if command == 'buy':
        break
    info = command.split()
    product = info[0]
    price = float(info[1])
    quantity = int(info[2])
    if product not in dictionary:
        dictionary[product] = []
        dictionary[product].append(price)
        dictionary[product].append(quantity)
    else:
        dictionary[product][0] = price
        dictionary[product][1] += quantity

for key, value in dictionary.items():
    x, y = value[0], value[1]
    result = x * y
    print(f'{key} -> {result:.2f}')
