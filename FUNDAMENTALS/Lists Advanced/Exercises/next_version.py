version = list(map(int, input().split('.')))
if version[2] < 9:
    version[2] += 1
else:
    version[2] = 0
    version[1] += 1
    if version[1] == 10:
        version[1] = 0
        version[0] += 1
print(f'{version[0]}.{version[1]}.{version[2]}')