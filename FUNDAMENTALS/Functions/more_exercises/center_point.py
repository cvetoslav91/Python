from math import floor

def center_point(x1, y1, x2, y2):
    minimum_number = min(abs(x1), abs(x2), abs(y1), abs(y2))
    if minimum_number == x1 or minimum_number == y1:
        return f"({x1}, {y1})({x2}, {y2})"
    else:
        return f"({x2}, {y2})({x1}, {y1})"


a = float(input())
b = float(input())
c = float(input())
d = float(input())
print(center_point(a, b, c, d))