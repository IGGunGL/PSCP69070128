"""Season"""
month = int(input())
day = int(input())
if (month in [1, 2]) or (month == 12 and day >= 21) or (month == 3 and day <= 20):
    print("winter")
elif (month in [4, 5]) or (month == 3 and day >= 21) or (month == 6 and day <= 20):
    print("spring")
elif (month in [7, 8]) or (month == 6 and day >= 21) or (month == 9 and day <= 20):
    print("summer")
elif (month in [10, 11]) or (month == 9 and day >= 21) or (month == 12 and day <= 20):
    print("fall")
else:
    print("error")
