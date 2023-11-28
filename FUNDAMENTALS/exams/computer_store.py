total_price = 0
taxes = 0
single_tax = 0.2
final_price = 0
while True:
    part = input()
    if part == 'special':
        final_price *= 0.9
        break
    if part == 'regular':
        break
    if float(part) < 0:
        print('Invalid price!')
        continue
    part = float(part)
    total_price += part
    current_tax = part * single_tax
    taxes += current_tax
    final_price = total_price + taxes
if final_price == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {final_price:.2f}$')
