"""Safelocked"""
Char = input()
digit = input()

if Char == "H" and digit == "4567":
    print("safe unlocked")
elif Char == "H" and digit != "4567":
    print("safe locked - change digit")
elif Char != "H" and digit == "4567":
    print("safe locked - change char")
else:
    print("safe locked")
