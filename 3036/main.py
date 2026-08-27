"""Pyramid Treasure Room"""
import math
n_room = int(input())
r = math.isqrt(n_room - 1) + 1
k = n_room - (r - 1) ** 2
if k % 2 == 1:
    walls = 2 * (r - 1)
else:
    walls = 2 * (r - 1) - 1
print(walls)
