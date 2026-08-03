"""GL"""
degree = float(input())
O = str(input()).upper()
N = str(input()).upper()

celcius = 0.0
if O == "C":
    celcius = degree
elif O == "K":
    celcius = degree - 273.15
elif O == "F":
    celcius = (degree - 32) * 5 / 9
elif O == "R":
    celcius = (degree - 491.67) * 5 / 9

result = 0.0
if N == "C":
    result = celcius
elif N == "K":
    result = celcius + 273.15
elif N == "F":
    result = celcius * 9 / 5 + 32
elif N == "R":
    result = (celcius + 273.15)*9/5
print(f"{result:.2f}")
