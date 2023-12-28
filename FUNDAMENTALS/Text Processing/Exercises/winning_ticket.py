def count_consecutive(symbol, word):
    current_count = 0
    total_count = 0
    counts = []
    for char in word:
        if char == symbol:
            current_count += 1
        else:
            current_count = 0
        counts.append(current_count)
    max_counts = max(counts)
    return max_counts


tickets = input().split(',')
new_tickets = [x.strip() for x in tickets]
for current_ticket in new_tickets:
    if len(current_ticket) != 20:
        print('invalid ticket')
        continue
    first_half = current_ticket[:10]
    second_half = current_ticket[10:]
    if '@' * 6 in first_half and '@' * 6 in second_half:
        win = min(count_consecutive('@', first_half), count_consecutive('@', second_half))
        if win == 10:
            print(f'ticket "{current_ticket}" - 10@ Jackpot!')
        else:
            print(f'ticket "{current_ticket}" - {win}@')
    elif '#' * 6 in first_half and '#' * 6 in second_half:
        win = min(count_consecutive('#', first_half), count_consecutive('#', second_half))
        if win == 10:
            print(f'ticket "{current_ticket}" - 10# Jackpot!')
        else:
            print(f'ticket "{current_ticket}" - {win}#')
    elif '$' * 6 in first_half and '$' * 6 in second_half:
        win = min(count_consecutive('$', first_half), count_consecutive('$', second_half))
        if win == 10:
            print(f'ticket "{current_ticket}" - 10$ Jackpot!')
        else:
            print(f'ticket "{current_ticket}" - {win}$')
    elif '^' * 6 in first_half and '^' * 6 in second_half:
        win = min(count_consecutive('^', first_half), count_consecutive('^', second_half))
        if win == 10:
            print(f'ticket "{current_ticket}" - 10^ Jackpot!')
        else:
            print(f'ticket "{current_ticket}" - {win}^')
    else:
        print(f'ticket "{current_ticket}" - no match')