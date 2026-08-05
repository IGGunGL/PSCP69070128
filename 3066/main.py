"""เหมือนกันหมด"""
num1 , num2 , num3 = int(input()) , int(input()) , int(input())
if num1 == num2 == num3:
    print("all the same")
elif num1 != num2 and num1 != num3 and num2 != num3:
    print("all different")
else:
    print("neither")
