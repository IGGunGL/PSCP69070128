"""coke"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if not b or not d:
    print(d * a)
else:
    promo = (d - 1) // b
    print((d * a) - promo * (a - c))
