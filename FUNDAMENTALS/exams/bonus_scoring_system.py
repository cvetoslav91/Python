from math import ceil
students = int(input())
total_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_lectures = 0
for current_student in range(students):
    current_student_attendances = int(input())
    total_bonus = current_student_attendances / total_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_lectures = current_student_attendances
print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_lectures} lectures.")