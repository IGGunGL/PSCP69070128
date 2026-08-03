"""ค่าสูงสุด"""
num1 = int(input())
num2 = int(input())
num3 = int(input())
all_num = [num1,num2,num3]
max_value = all_num[0]
for num in all_num:
    if num > max_value:
        max_value = num
print(max_value)
