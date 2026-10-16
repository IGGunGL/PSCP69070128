"""รหัสต้องไม่ซ้ำกัน"""

def main():
    """main"""
    _ = input()
    relics = list(map(int, input().split()))
    counts = {}
    for num in relics:
        counts[num] = counts.get(num, 0) + 1
    singles = sorted(x for x, c in counts.items() if c == 1)
    print(*singles)

if __name__ == '__main__':
    main()
