"""เข้าแถว"""

def main():
    """main"""
    n, _ = map(int, input().split())
    heights = [0] + list(map(int, input().split()))
    customers = list(map(int, input().split()))

    pref_max = [0] * (n + 1)
    for i in range(1, n + 1):
        pref_max[i] = max(pref_max[i - 1], heights[i])

    for aj in customers:
        if aj == 1:
            print(0)
        else:
            max_front = pref_max[aj - 1]
            if heights[aj] > max_front:
                print(0)
            else:
                print(max_front + 1 - heights[aj])

if __name__ == '__main__':
    main()
