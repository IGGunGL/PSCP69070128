"""GL"""
name = input()
surname = input()
age = int(input())
if len(name) >= 5 and len(surname) >= 5:
    print(name[0:2]+surname[-1]+str(age)[-1])
else:
    print(name[0]+str(age)+surname[-1])
