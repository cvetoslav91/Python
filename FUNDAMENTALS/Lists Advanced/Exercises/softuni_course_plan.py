courses = input().split(', ')
while True:
    command = input().split(':')
    if 'course start' in command:
        break
    if command[0] == 'Add' and command[1] not in courses:
        courses.append(command[1])
    elif command[0] == 'Insert' and command[1] not in courses:
        courses.insert(int(command[2]), command[1])
    elif command[0] == 'Remove' and command[1] in courses:
        courses.remove(command[1])
        if command[1] + '-Exercise' in courses:
            courses.remove(command[1] + '-Exercise')
    elif command[0] == 'Swap' and command[1] in courses and command[2] in courses:
        index_of_first = courses.index(command[1])
        index_of_second = courses.index(command[2])
        courses[index_of_first], courses[index_of_second] = courses[index_of_second], courses[index_of_first]
        if command[1] + '-Exercise' in courses and command[2] + '-Exercise'  not in courses:
            index_of_command = courses.index(command[1])
            courses.remove(command[1]+'-Exercise')
            courses.insert(index_of_command + 1, command[1]+'-Exercise')
        elif command[2] + '-Exercise' in courses and command[1] + '-Exercise' not in courses:
            index_of_command = courses.index(command[2])
            courses.remove(command[2] + '-Exercise')
            courses.insert(index_of_command + 1, command[2] + '-Exercise')
        elif command[1] + '-Exercise' in courses and command[2] + '-Exercise' in courses:
            index1 = courses.index(command[1] + '-Exercise')
            index2 = courses.index(command[2] + '-Exercise')
            courses[index1], courses[index2] = courses[index2], courses[index1]
    elif command[0] == 'Exercise' and command[1] + '-Exercise' not in courses:
        if command[1] in courses:
            index_of_course = courses.index(command[1])
            courses.insert(index_of_course + 1, command[1] + '-Exercise')
        else:
            courses.append(command[1])
            courses.append(command[1]+'-Exercise')
i = 1
for course in courses:
    print(f'{i}.{course}')
    i += 1


