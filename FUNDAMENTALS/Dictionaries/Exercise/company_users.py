dictionary = {}
while True:
    info = input()
    if info == 'End':
        break
    company_name, employee_id = info.split(' -> ')
    if company_name not in dictionary:
        dictionary[company_name] = []
    if employee_id not in dictionary[company_name]:
        dictionary[company_name].append(employee_id)
    else:
        continue

for key, value in dictionary.items():
    print(key)
    for i in value:
        print(f'-- {i}')