stack = []

n = int(input())

for _ in range(n):
    number = input().split()
    if len(number) == 2:
        stack.append(int(number[1]))
    else:
        current_number = int(number[0])
        if stack:
            if current_number == 2:
                stack.pop()
            elif current_number == 3:
                print(max(stack))
            elif current_number == 4:
                print(min(stack))

result = stack[-1::-1]
print(', '.join(map(str, result)))