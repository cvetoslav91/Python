items = input().split(', ')
while True:
    command = input().split(' - ')
    if command[0] == "Craft!":
        break
    elif command[0] == 'Collect':
        new_item = command[1]
        if new_item in items:
            continue
        else:
            items.append(new_item)
    elif command[0] == 'Drop':
        new_item = command[1]
        if new_item in items:
            items.remove(new_item)
    elif command[0] == 'Combine Items':
        items_list = command[1].split(':')
        old_item = items_list[0]
        new_item = items_list[1]
        if old_item in items:
            index_of_old_item = items.index(old_item)
            items.insert(index_of_old_item + 1, new_item)

    elif command[0] == 'Renew':
        the_item = command[1]
        if the_item in items:
            index = items.index(the_item)
            removed_item = items.pop(index)
            items.append(removed_item)
print(', '.join(items))