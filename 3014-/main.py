"""Milk"""
a = int(input())  #ราคาขวดละ
b = int(input())  #ใช้กี่ฝาแลก
c = int(input())  #ได้นมฟรีกี่ขวด
d = int(input())  #เงินที่มี

total = d // a
caps = total
if b > 0 and c > 0:
    while caps >= b:
        new_milk = (caps // b) * c
        total += new_milk
        caps = (caps % b) + new_milk

print(total)
