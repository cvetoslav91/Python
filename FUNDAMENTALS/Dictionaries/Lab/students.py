students_dictionary = {}
while True:
    command = input()
    if ':' not in command:
        break
    students_info = command.split(':')
    name, ID, course = students_info[0], students_info[1], students_info[2]
    students_dictionary[name] = [ID, course]
for key, value in students_dictionary.items():
    if value[1].startswith(command[0:3]):
        print(f'{key} - {value[0]}')



