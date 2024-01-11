import re

string = input()
pattern = r'(#|\|)([a-zA-Z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)'
result = re.findall(pattern, string)
dictionary = []
total_calories = 0
for match in result:
    product = match[1]
    date = match[3]
    calories = int(match[5])
    total_calories += calories
    dictionary.append(product)
    dictionary.append(date)
    dictionary.append(calories)

days_left = total_calories // 2000

print(f"You have food to last you for: {days_left} days!")
for i in range(0, len(dictionary), 3):
    print(f"Item: {dictionary[i]}, Best before: {dictionary[i + 1]}, Nutrition: {dictionary[i + 2]}")