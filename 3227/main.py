"""ระบบคิดคะแนนออนไลน์"""
def main():
    """ไพ่"""
    card = input().upper()

    suit = card[-1]
    rank = card[:-1]

    if rank == "A":
        rankname = "ace"
    elif rank == "J":
        rankname = "jack"
    elif rank == "Q":
        rankname = "queen"
    elif rank == "K":
        rankname = "king"
    else:
        rankname = rank

    if suit == "D":
        suitname = "diamonds"
    elif suit == "H":
        suitname = "hearts"
    elif suit == "S":
        suitname = "spades"
    else:
        suitname = "clubs"

    print(rankname, "of", suitname)

main()
