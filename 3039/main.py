"""ค่าสูงสุด"""
n = int(input())
low_value = int(input())
for n in range(n - 1):
    num = int(input())
    if num < low_value:
        low_value = num
print(low_value)
