"""Elo"""
Ra = int(input())
Rb = int(input())
Elo = input()
Ea = 1 / (1 + 10 ** ((Rb-Ra) / 400))
Eb = 1 / (1 + 10 ** ((Ra-Rb) / 400))

if Elo == "A":
    print(f"{Ea:.2f}")
elif Elo == "B":
    print(f"{Eb:.2f}")
