"""เกมทายลูกเต๋า"""
guest = int(input())
real = int(input())

if not (1 <= guest <= 6 and 1 <= real <= 6):
    print("Invalid")
elif guest == real:
    print("Correct!")
elif guest != real:
    print("Wrong!")
