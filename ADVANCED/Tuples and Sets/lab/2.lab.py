number = int(input())
students = {}
for _ in range(number):
    student, grade = input().split()
    grade = float(grade)
    if student not in students:
        students[student] = []
    students[student].append(grade)

for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    print(f"{name} -> ", end='')
    for grade in grades:
        print(f'{grade:.2f}', end=' ')
    print(f'(avg: {average_grade:.2f})')