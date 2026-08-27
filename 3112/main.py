"""ชานมไข่มุก"""
Boba , amount = input().split()
Tea , sweet , amtea = input().split()
sumboba = 0
sumtea = 0
if Boba == "H":
    sumboba += 5 * float(amount)
elif Boba == "M":
    sumboba += 3 * float(amount)
elif Boba == "J":
    sumboba += 2 * float(amount)

if Tea == "R" and sweet == "1":
    sumtea += 12
elif Tea == "R" and sweet == "2":
    sumtea += 18
elif Tea == "R" and sweet == "3":
    sumtea += 25

if Tea == "T" and sweet == "1":
    sumtea += 15
elif Tea == "T" and sweet == "2":
    sumtea += 20
elif Tea == "T" and sweet == "3":
    sumtea += 30

if Tea == "M" and sweet == "1":
    sumtea += 10
elif Tea == "M" and sweet == "2":
    sumtea += 15
elif Tea == "M" and sweet == "3":
    sumtea += 20

print(f"{sumboba + (sumtea * int(amtea)):g}")
