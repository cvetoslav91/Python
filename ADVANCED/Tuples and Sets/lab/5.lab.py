n = int(input())
guests_to_come = set()
who_came = set()

for _ in range(n):
    code = input()
    guests_to_come.add(code)

command = input()
while command != 'END':
    who_came.add(command)
    command = input()
result = sorted(guests_to_come.difference(who_came))
print(len(result))
print(*result, sep='\n')