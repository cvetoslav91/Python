items = input().split('|')
while True:
    command = input().split()
    if command[0] == "Yohoho!":
        break
    if command[0] == 'Loot':
        for i in range(1, len(command)):
            new_item = command[i]
            if new_item not in items:
                items.insert(0, new_item)
    elif command[0] == 'Drop':
        index = int(command[1])
        if index < 0 or index >= len(items):
            continue
        else:
            removed_item = items.pop(index)
            items.append(removed_item)
    elif command[0] == 'Steal':
        value = int(command[1])
        items.reverse()
        stealed_items = items[:value]
        items = items[value:]
        stealed_items.reverse()
        print(', '.join(stealed_items))
        items.reverse()
if not items:
    print("Failed treasure hunt.")
else:
    total_sum = 0
    for item in items:
        total_sum += len(item)
    avg_treasure_gain = total_sum / len(items)
    print(f"Average treasure gain: {avg_treasure_gain:.2f} pirate credits.")