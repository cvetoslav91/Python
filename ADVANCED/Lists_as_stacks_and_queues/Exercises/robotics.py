from datetime import timedelta, datetime
from collections import deque

robots = {}

data = [x for x in input().split(';')]
for info in data:
    robot, seconds = info.split('-')
    robots[robot] = [int(seconds), 0]
time = input()
current_time = datetime.strptime(time, '%H:%M:%S')
details = deque()
while True:
    detail = input()
    if detail == 'End':
        break

    details.append(detail)

while details:
    current_detail = details.popleft()
    current_time += timedelta(seconds=1)

    free_robots = []
    for name, info in robots.items():
        if info[1] != 0:
            robots[name][1] -= 1
        if info[1] == 0:
            free_robots.append([name, info])

    if not free_robots:
        details.append(current_detail)
        continue

    robots_name, data = free_robots[0]
    robots[robots_name][1] = data[0]
    ctime = current_time.strftime('%H:%M:%S')
    print(f'{robots_name} - {current_detail} [{ctime}]')

