"""factorial"""
num = int(input())
fact = 1
if not num:
    print("1")
else:
    for i in range(1, num + 1):
        fact *= i
    print(fact)
