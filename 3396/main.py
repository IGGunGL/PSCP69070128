"""แซงรอบ"""

def main():
    """main"""
    n, k = map(int, input().split())
    times = [int(input()) for _ in range(n)]

    if k <= 1:
        print(n)
        return

    s_win = min(times)
    target = k * s_win
    count = 0
    for s in times:
        if s * (k - 1) < target:
            count += 1

    print(count)

if __name__ == '__main__':
    main()
