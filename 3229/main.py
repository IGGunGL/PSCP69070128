"""ระบบคิดคะแนนเกมออนไลน์"""


def main():
    """คำนวณคะแนนรวมและสถานะพิเศษ"""
    base = float(input())
    bonus = float(input())
    days = int(input())

    multiplier = 1.5 if days > 3 else 1.0
    total = (base + bonus) * multiplier

    if total >= 1500:
        rank = 5
    elif total >= 1000:
        rank = 4
    elif total >= 500:
        rank = 3
    elif total >= 200:
        rank = 2
    else:
        rank = 1

    if rank == 5 and days >= 7:
        special = 99
    elif rank == 4 and bonus > 300:
        special = 88
    else:
        special = 0

    print(int(total))
    print(rank)
    print(special)

main()
