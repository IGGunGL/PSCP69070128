"""ลอดสะพาน"""

def main():
    """main"""
    l, n = map(int, input().split())
    bridges = []
    for _ in range(n):
        a, b = map(int, input().split())
        bridges.append((a, b))

    max_bridges = 0
    for k in range(l):
        mid = k + 0.5
        count = sum(1 for a, b in bridges if a < mid < b)
        max_bridges = max(max_bridges, count)

    print(max_bridges)

if __name__ == '__main__':
    main()
