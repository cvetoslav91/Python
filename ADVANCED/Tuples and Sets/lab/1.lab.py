numbers = input().split()
same_numbers = set()
for number in numbers:
    if number not in same_numbers:
        same_numbers.add(number)
        occ = numbers.count(number)
        number = float(number)
        print(f"{number:.1f} - {occ} times")