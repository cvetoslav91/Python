def softuni_students(*course_student, **courseinfo):
    students = {}
    invalid = []
    for id, name in course_student:
        for key, value in courseinfo.items():
            if id == key:
                students[name] = value
                break
        else:
            invalid.append(name)
    sorted_students = sorted(students.items())
    result = ''
    for name, course in sorted_students:
        result += f"*** A student with the username {name} has successfully finished the course {course}!\n"
    if invalid:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid))}"
    return result


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))