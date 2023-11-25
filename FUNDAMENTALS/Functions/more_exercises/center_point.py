from math import floor

def center_point(x1, y1, x2, y2):
    minimum_number = min(abs(x1), abs(x2), abs(y1), abs(y2))
    if minimum_number == x1 or minimum_number == y1:
        return f"({floor(x1)}, {floor(y1)})"
    else:
        return f"({floor(x2)}, {floor(y2)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(center_point(x1, y1, x2, y2))