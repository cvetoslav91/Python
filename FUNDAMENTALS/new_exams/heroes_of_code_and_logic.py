def cast_spell(hero, mp_needed, spell_name):
    if mp_needed <= heroes[hero][1]:
        heroes[hero][1] -= mp_needed
        return f"{hero} has successfully cast {spell_name} and now has {heroes[hero][1]} MP!"
    return f"{hero} does not have enough MP to cast {spell_name}!"


def take_damage(hero_name, damage, attacker):
    heroes[hero_name][0] -= damage
    if heroes[hero_name][0] <= 0:
        del heroes[hero_name]
        return f"{hero_name} has been killed by {attacker}!"
    return f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!"


def recharge(hero_name, amount):
    if heroes[hero_name][1] + amount > 200:
        amount = 200 - heroes[hero_name][1]
        heroes[hero_name][1] = 200
    else:
        heroes[hero_name][1] += amount
    return f"{hero_name} recharged for {amount} MP!"


def heal(hero_name, amount):
    if heroes[hero_name][0] + amount > 100:
        amount = 100 - heroes[hero_name][0]
        heroes[hero_name][0] = 100
    else:
        heroes[hero_name][0] += amount
    return f"{hero_name} healed for {amount} HP!"


number_of_heroes = int(input())

heroes = {}

for i in range(number_of_heroes):
    name, hp, mp = input().split()
    hp, mp = int(hp), int(mp)
    if hp > 100:
        hp = 100
    if mp > 200:
        mp = 200

    heroes[name] = [hp, mp]


while True:
    command = input().split(' - ')

    if command[0] == 'End':
        break

    elif command[0] == 'CastSpell':
        print(cast_spell(command[1], int(command[2]), command[3]))

    elif command[0] == 'TakeDamage':
        print(take_damage(command[1], int(command[2]), command[3]))

    elif command[0] == 'Recharge':
        print(recharge(command[1], int(command[2])))

    elif command[0] == 'Heal':
        print(heal(command[1], int(command[2])))

for name, info in heroes.items():
    print(f'{name}\n  HP: {info[0]}\n  MP: {info[1]}')