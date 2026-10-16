"""Name of Card"""

def main():
    """main"""
    code = input().strip()
    suit_char = code[-1].upper()
    rank_str = code[:-1].upper()

    ranks = {
        "A": "Ace", "J": "Jack", "Q": "Queen", "K": "King"
    }
    suits = {
        "D": "Diamonds", "H": "Hearts", "S": "Spades", "C": "Clubs"
    }

    rank_name = ranks.get(rank_str, rank_str)
    suit_name = suits[suit_char]
    print(f"{rank_name} of {suit_name}")

if __name__ == '__main__':
    main()
