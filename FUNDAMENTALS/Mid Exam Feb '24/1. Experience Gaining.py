needed_exp = float(input())
battles = int(input())

total_exp = 0

for battle in range(1, battles + 1):
    current_exp = float(input())

    if battle % 3 == 0:
        current_exp *= 1.15

    if battle % 5 == 0:
        current_exp *= 0.9

    total_exp += current_exp

    if total_exp >= needed_exp:
        print(f'Player successfully collected his needed experience for {battle} battles.')
        break

else:
    diff = needed_exp - total_exp
    print(f'Player was not able to collect the needed experience, {diff:.2f} more needed.')
