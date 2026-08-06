"""ค่าน้อยที่สุด"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
ans = num1
if num2 < ans:
    ans = num2
if num3 < ans:
    ans = num3

print(ans)
