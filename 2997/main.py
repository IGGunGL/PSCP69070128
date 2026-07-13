"""GL"""
RA = int(input())
RB = int(input())
Elo = input()

EA = 1 / (1 + 10**((RB - RA) / 400))
EB = 1 / (1 + 10**((RA - RB) / 400))

if Elo == "A":
    print(f"{EA:.2f}")
elif Elo == "B":
    print(f"{EB:.2f}")
