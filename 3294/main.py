"""Teach schedule"""
classweek = int(input())
time = int(input())
vera = classweek * time
hour = vera // 60
minute = vera % 60
if not hour and not minute:
    print("No teaching")
elif not hour:
    print(minute, "minute")
elif not minute:
    print(hour,"hours")
else:
    print(hour,"hours" , minute, "minute")
