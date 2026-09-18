"""right arrow"""
k = int(input())
n = int(input())

for i in range(n):
    print(" " *(n//2 - abs(n//2-i)) + "*" *k)
