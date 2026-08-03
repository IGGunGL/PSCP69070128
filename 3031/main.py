"""Ink"""
import math
ink , house = map(int,input().split())

for i in range(house):
    i=i+1
    x , y = map(int,input().split())
    s = 3.1416 * (x**2 + y**2)
    t = s/ink
    print(math.ceil(t))
