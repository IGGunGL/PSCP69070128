"""วันเกิด"""
from datetime import date
y1, m1, d1 = int(input()), int(input()), int(input())
y2, m2, d2 = int(input()), int(input()), int(input())

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

if abs((date1 - date2).days) <= 7:
    print(0)
elif date1 < date2:
    print(1)
else:
    print(2)
