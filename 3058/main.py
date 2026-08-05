"""Bridgebrick"""
a = int(input())
b = int(input())
goal = int(input())
big_need = goal // 5
if b < big_need:
    big_used = b
else:
    big_used = big_need

small_need = goal - (big_used * 5)

if a >= small_need:
    print(small_need)
else:
    print(-1)
