"""GL"""
a = float(input())
b = float(input())
c = float(input())
triangle = (a + b + c) / 2
area = (triangle * (triangle - a) * (triangle - b) * (triangle - c)) ** 0.5
print(f"{area:.3f}")
