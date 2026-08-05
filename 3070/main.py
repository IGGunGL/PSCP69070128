"""นับคู่คี่"""
n1 = int(input())
n2 = int(input())
n3 = int(input())
even = (not n1 % 2) + (not n2 % 2) + (not n3 % 2)
odd = 3 - even

print(even)
print(odd)
