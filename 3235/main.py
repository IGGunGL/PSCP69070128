"""กระต่ายอ้วน"""
num = int(input())
fat = 0
max_weight = -1
fattest = ""

for i in range(num):
    i = i-0
    name, weight = input().split()
    weightint = int(weight)
    if weightint > 15:
        fat += 1
    if weightint > max_weight:
        max_weight = weightint
        fattest = name

print(fat)
print(fattest)
