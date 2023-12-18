dictionary_of_students = {}
dictionary_of_courses = {}
while True:
    info = input()
    if info == 'exam finished':
        break
    students_info = info.split('-')
    if students_info[1] == 'banned':
        del dictionary_of_students[students_info[0]]
        continue
    name, course, points = info.split('-')
    if course in dictionary_of_courses:
        dictionary_of_courses[course] += 1
    else:
        dictionary_of_courses[course] = 1
    if name not in dictionary_of_students or int(dictionary_of_students[name][1]) < int(points):
        dictionary_of_students[name] = (course, points)
print(f"Results:")
for key, value in dictionary_of_students.items():
    print(f'{key} | {value[1]}')

print(f"Submissions:")
for key, value in dictionary_of_courses.items():
    print(f'{key} - {value}')