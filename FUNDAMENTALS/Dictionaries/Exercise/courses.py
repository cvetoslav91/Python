dictionary = {}
while True:
    command = input()
    if command == 'end':
        break
    course, student = command.split(' : ')
    if course not in dictionary:
        dictionary[course] = []
    dictionary[course].append(student)

for key, value in dictionary.items():
    print(f"{key}: {len(value)}")
    for student in value:
        print(f"-- {student}")
