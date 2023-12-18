dictionary = {}
flag = False
while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if '|' in command:
        force_side, force_user = command.split(' | ')
        if force_side not in dictionary:
            dictionary[force_side] = []
        for value in dictionary.values():
            if force_user in value:
                flag = True
                break
        if flag:
            flag = False
            continue
        dictionary[force_side].append(force_user)
    elif '->' in command:
        force_user, force_side = command.split(' -> ')
        if force_side not in dictionary:
            dictionary[force_side] = []
        for value in dictionary.values():
            if force_user in value:
                value.remove(force_user)
        dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")


for key, value in dictionary.items():
    if len(value) == 0:
        continue
    print(f"Side: {key}, Members: {len(value)}")
    for member in value:
        print(f'! {member}')
