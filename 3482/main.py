"""นักล่าอสูร"""

def main():
    """main"""
    demon_list = [
        ("Spider Demon", 1),
        ("Swamp Demon", 2),
        ("Arrow Demon", 1),
        ("Hand Demon", 2),
        ("Drum Demon", 3),
        ("Mugen Train", 2),
        ("Upper Moon", 3),
    ]

    queue = list(demon_list)
    killed = 0
    total_attacks = 0

    while killed < 5 and queue:
        name, hp = queue.pop(0)
        print(name)
        is_killed = False
        for _ in range(2):
            val = int(input())
            total_attacks += 1
            if val == hp:
                print("kill")
                killed += 1
                is_killed = True
                break
        if not is_killed:
            print("back")
            queue.append((name, hp))

    print(total_attacks)

if __name__ == '__main__':
    main()
