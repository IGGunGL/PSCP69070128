"""Bonus"""
role, age, salary = input().split()
role = role.upper()
age = float(age)
salary = float(salary)
bonus = 0

if role == "M":
    if age <= 5:
        bonus = 1500 + (salary * 6 / 100)
    elif age <= 10:
        bonus = 1500 + (salary * 8 / 100)
    else:
        bonus = 1500 + (salary * 10 / 100)

elif role == "B":
    if age <= 5:
        bonus = 1000 + (salary * 5 / 100)
    elif age <= 10:
        bonus = 1000 + (salary * 6 / 100)
    else:
        bonus = 1000 + (salary * 7 / 100)

elif role == "G":
    if age <= 5:
        bonus = 500 + (salary * 4 / 100)
    elif age <= 10:
        bonus = 500 + (salary * 5 / 100)
    else:
        bonus = 500 + (salary * 6 / 100)

print(int(round(bonus)))
