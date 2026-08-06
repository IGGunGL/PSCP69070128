"""Ticket"""
age_str, day = input().split()
age = int(age_str)
if age < 5:
    price = 0
elif age <= 18:
    price = 100
else:
    price = 150
if day == "Wed":
    price = price // 2

print(int(price))
