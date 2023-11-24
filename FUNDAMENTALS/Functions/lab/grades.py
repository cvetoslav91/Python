# •	2.00 – 2.99 - "Fail"
# •	3.00 – 3.49 - "Poor"
# •	3.50 – 4.49 - "Good"
# •	4.50 – 5.49 - "Very Good"
# •	5.50 – 6.00 - "Excellent"
def grade(n):
    if 2 <= n <= 2.99:
        return 'Fail'
    elif 3 <= n <= 3.49:
        return 'Poor'
    elif 3.50 <= n <= 4.49:
        return 'Good'
    elif 4.5 <= n <= 5.49:
        return 'Very Good'
    elif 5.5 <= n <= 6:
        return 'Excellent'

n = float(input())
print(grade(n))