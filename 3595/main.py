"""Meteor"""
a = float(input())
b = int(input())
c = float(input())

countshoot = 0
count = 1
weight = a

while weight >= c:
    countshoot += count
    count *= b
    weight /= b

print(countshoot)
