import copy
contests = {}
while True:
    new_contest = input()
    if new_contest == "end of contests":
        break
    contest, password = new_contest.split(':')
    contests[contest] = password

students = {}
while True:
    submissions = input()
    if submissions == "end of submissions":
        break
    contest, password, username, points = submissions.split('=>')
    points = int(points)
    for key,value in contests.items():
        if contest == key and password == value:
            if username not in students:
                students[username] = {contest: points}
                break
            else:
                if contest in students[username]:
                    if students[username][contest] < points:
                        students[username][contest] = points
                else:
                    students[username][contest] = points

new_dict = dict(sorted(students.items(), key=lambda x: x[0]))
final_dictionary = {}
for key, value in new_dict.items():
    sorted_data = dict(sorted(new_dict[key].items(), key=lambda x: x[1], reverse=True))
    curr_dict = {key: sorted_data}
    final_dictionary.update(curr_dict)

points_dictionary = {}
max_points = 0
best_candidate = ''
for key, value in final_dictionary.items():
    total_points = 0
    for points in value.values():
        total_points += points
    if total_points > max_points:
        max_points = total_points
        best_candidate = key

print(f'Best candidate is {best_candidate} with total {max_points} points.')
print('Ranking:')
for name, info in final_dictionary.items():
    print(name)
    for course, points in info.items():
        print(f'#  {course} -> {points}')