first_employee_student_per_hour = int(input())
second_employee_student_per_hour = int(input())
third_employee_student_per_hour = int(input())
students_count = int(input())
hours = 0
counter = 0
students_per_hour = first_employee_student_per_hour + second_employee_student_per_hour + third_employee_student_per_hour
while students_count > students_per_hour:
    students_count -= students_per_hour
    hours += 1
    counter += 1
    if counter == 3:
        hours += 1
        counter = 0
if students_count > 0:
    hours += 1
print(f"Time needed: {hours}h.")
