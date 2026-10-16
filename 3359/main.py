"""กองชาม"""

def main():
    """main"""
    n = int(input())
    counts = {}
    for _ in range(n):
        bowl = input().strip()
        counts[bowl] = counts.get(bowl, 0) + 1
    print(max(counts.values()))

if __name__ == '__main__':
    main()
