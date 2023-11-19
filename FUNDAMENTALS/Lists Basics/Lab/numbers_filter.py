n = int(input())
even = []
odd = []
positive = []
negative = []
for number in range(n):
    current_number = int(input())
    if current_number % 2 == 0:
        even.append(current_number)
    else:
        odd.append(current_number)
    if current_number >= 0:
        positive.append(current_number)
    else:
        negative.append(current_number)
command = input()
if command == 'even':
    print(even)
elif command == 'odd':
    print(odd)
elif command == 'positive':
    print(positive)
elif command == 'negative':
    print(negative)