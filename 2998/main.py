"""Eucliden distance รับค่าพิกัด 2 จุดหาระยะทาง"""
q1 = float(input())
q2 = float(input())
p1 = float(input())
p2 = float(input())

d = ( (q1 - p1) ** 2 + (q2 - p2) ** 2 ) ** 0.5 #**0.5 คือรูท
print(d) 
