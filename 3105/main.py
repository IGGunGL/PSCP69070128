"""TAXI"""
km = int(input())
price = 0
if not km:
    price=0
elif km == 1:
    price=35
elif 1 < km <= 10:
    price=(km-1)*5+35
else:
    price=(km-10)*8+80
print(price)
