"""Triangle"""
n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print("0")
    elif i == n:
        print("0" * n)
    else:
        print("0" + ("1" * (i - 2)) + "0")
