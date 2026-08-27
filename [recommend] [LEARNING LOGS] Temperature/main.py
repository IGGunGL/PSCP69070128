"""Temperature"""
degree = float(input())
old = input()
new = input()
celcius = 0.0

if old == "C":
    celcius = degree
elif old == "K":
    celcius = degree - 273.15
elif old == "F":
    celcius = (degree - 32) * 5 / 9
elif old == "R":
    celcius = (degree - 491.67) * 5 / 9

result = 0.0

if new == "C":
    result = celcius
elif new == "K":
    result = celcius + 273.15
elif new == "F":
    result = celcius * 9 / 5 + 32
elif new == "R":
    result = (celcius + 273.15)*9/5
print(f"{result:.2f}")
