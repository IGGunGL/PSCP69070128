"""เช็กผลสอบ"""
exam = int(input())
midterm = int(input())
final = int(input())

if exam > 10:
    exam = 10
elif midterm > 40:
    midterm = 40
elif final > 50:
    final = 50

if exam >= 5 and midterm >= 20 and final >= 25:
    print("pass")
else:
    print("fail")
