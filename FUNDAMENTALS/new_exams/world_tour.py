def add_stops(text, index, string):
    if len(text) - 1 >= index:
        text = text[:index] + string + text[index:]
        return text
    else:
        return text

def remove_stop(text, start_index, end_index):
    if len(text) - 1 >= end_index:
        text = text[:start_index] + text[end_index + 1:]
        return text
    else:
        return text

def switch(text, old_string, new_string):
    while old_string in text:
        text = text.replace(old_string, new_string)
        return text
    return text

all_stops = input()
while True:
    commands = input()
    if commands == 'Travel':
        break
    else:
        command, first_info, second_info = commands.split(':')
    if command == 'Add Stop':
        index = int(first_info)
        string = second_info
        all_stops = add_stops(all_stops, index, string)
    elif command == 'Remove Stop':
        start_index = int(first_info)
        end_index = int(second_info)
        all_stops = remove_stop(all_stops, start_index, end_index)
    elif command == 'Switch':
        all_stops = switch(all_stops, first_info, second_info)
    print(all_stops)
print(f"Ready for world tour! Planned stops: {all_stops}")