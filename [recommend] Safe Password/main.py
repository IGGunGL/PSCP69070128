"""safelocked"""
char = input()
num = input()

CORRECT_CHAR = "H"
CORRECT_NUM = "4567"

if char == CORRECT_CHAR:
    if num == CORRECT_NUM:
        print("safe unlocked")
    elif num != CORRECT_NUM:
        print("safe locked - change digit")

elif num == CORRECT_NUM:
    if char != CORRECT_CHAR:
        print("safe locked - change char")

else:
    print("safe locked")
