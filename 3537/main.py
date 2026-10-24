"""Impostor"""
import json

def main():
    """main"""
    players = {}
    while True:
        line = input().strip()
        if line == "Start":
            break
        data = json.loads(line)
        for name, role in data.items():
            players[name] = role

    dead_names = set()
    while True:
        line = input().strip()
        if line == "End":
            break
        dead_names.add(line)

    alive_players = []
    dead_players = []
    impostor_alive_count = 0

    for name in sorted(players):
        role = players[name]
        if name in dead_names:
            dead_players.append((name, role))
        else:
            alive_players.append((name, role))
            if role == "Impostor":
                impostor_alive_count += 1

    print(f"{impostor_alive_count} Impostor Remains")
    print("***Alive***")
    for name, role in alive_players:
        print(f"{name} : {role}")

    print("***Dead***")
    for name, role in dead_players:
        print(f"{name} : {role}")

if __name__ == '__main__':
    main()
