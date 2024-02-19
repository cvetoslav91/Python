vehicles = [vehicle for vehicle in input().split('>>')]

initial_tax = {
    'family': 50,
    'heavyDuty': 80,
    'sports': 100
}

total_taxes = 0

for info in vehicles:
    type, years, kms = info.split()
    if type == 'family':
        decrease_for_years = int(years) * 5
        increase_for_kms = (int(kms) // 3000) * 12
    elif type == 'heavyDuty':
        decrease_for_years = int(years) * 8
        increase_for_kms = (int(kms) // 9000) * 14
    elif type == 'sports':
        decrease_for_years = int(years) * 9
        increase_for_kms = (int(kms) // 2000) * 18
    else:
        print('Invalid car type.')
        continue

    total_amount = initial_tax[type] - decrease_for_years + increase_for_kms
    total_taxes += total_amount

    print(f'A {type} car will pay {total_amount:.2f} euros in taxes.')

print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")