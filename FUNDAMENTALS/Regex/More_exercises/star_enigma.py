import re

rows = int(input())
attacked_planets = []
destroyed_planets = []
for i in range(rows):
    current_row = input()
    result = re.findall(r'[star]', current_row, re.IGNORECASE)
    count = len(result)
    new_message_list = [chr(ord(x) - count) for x in current_row]
    new_message = ''.join(new_message_list)
    patt = r'@([a-zA-Z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*\!([AD])![^\@\-\!\:\>]*\-\>(\d+)'
    decrypted = re.findall(patt, new_message)
    if decrypted:
        for i in decrypted:
            name = i[0]
            count = i[1]
            type = i[2]
            soldiers = i[3]
        if type == 'A':
            attacked_planets.append(name)
        elif type == 'D':
            destroyed_planets.append(name)

attacked_planets = sorted(attacked_planets)
destroyed_planets = sorted(destroyed_planets)
print(f"Attacked planets: {len(attacked_planets)}")
if len(attacked_planets) > 0:
    for planet in attacked_planets:
        print(f'-> {planet}')
print(f"Destroyed planets: {len(destroyed_planets)}")
if len(destroyed_planets) > 0:
    for dplanet in destroyed_planets:
        print(f'-> {dplanet}')
