"""Duplicate I"""

def main():
    """main"""
    m = int(input())
    n = int(input())

    g1 = {input().strip() for _ in range(m)}
    g2 = {input().strip() for _ in range(n)}

    common = sorted(g1 & g2, reverse=True)
    if common:
        for cid in common:
            print(cid)
    else:
        print("Nope")

if __name__ == '__main__':
    main()
