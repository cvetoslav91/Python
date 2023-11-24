def orders(product, quantity: int):
    if product == 'coffee':
        price = 1.5
        result = price * quantity
        return result
    elif product == 'water':
        price = 1
        result = price * quantity
        return result
    elif product == 'coke':
        price = 1.4
        result = price * quantity
        return result
    elif product == 'snacks':
        price = 2
        result = price * quantity
        return result

product = input()
quantity = int(input())
result = orders(product, quantity)
print(f'{result:.2f}')
