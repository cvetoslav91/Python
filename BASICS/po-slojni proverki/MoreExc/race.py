juniors = int(input())
seniors = int(input())
type_of_race = input()

if type_of_race == 'trail':
    juniors_tax = 5.5 * juniors
    seniors_tax = 7 * seniors
    all_tax = juniors_tax + seniors_tax
    final_price = all_tax - (all_tax * 0.05)
    print(f'{final_price:.2f}')
elif type_of_race == 'cross-country':
    juniors_tax = 8 * juniors
    seniors_tax = 9.5 * seniors
    all_tax = juniors_tax + seniors_tax
    if juniors + seniors >= 50:
        all_tax = all_tax - (all_tax * 0.25)
    final_price = all_tax - (all_tax * 0.05)
    print(f'{final_price:.2f}')
elif type_of_race == 'downhill':
    juniors_tax = 12.25 * juniors
    seniors_tax = 13.75 * seniors
    all_tax = juniors_tax + seniors_tax
    final_price = all_tax - (all_tax * 0.05)
    print(f'{final_price:.2f}')
elif type_of_race == 'road':
    juniors_tax = 20 * juniors
    seniors_tax = 21.5 * seniors
    all_tax = juniors_tax + seniors_tax
    final_price = all_tax - (all_tax * 0.05)
    print(f'{final_price:.2f}')
