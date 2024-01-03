import re

dates = input()

pattern = r'\b(\d{2})([-.\/])([A-Z]{1}[a-z]{2})(\2)(\d{4})\b'

result = re.findall(pattern, dates)

for i in result:
    day = i[0]
    month = i[2]
    year = i[4]
    print(f"Day: {day}, Month: {month}, Year: {year}")