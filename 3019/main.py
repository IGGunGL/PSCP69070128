"""safeklock"""
char = input()
num = input()
if char == "H":
    if num == "4567":
        print("safe unlocked")
    else:
        print("safe locked - change digit")
else:
    if num == "4567":
        print("safe locked - change char")
    else:
        print("safe locked")
