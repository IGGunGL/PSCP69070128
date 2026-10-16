"""ติดตั้งหลอดไฟ"""

def main():
    """main"""
    n = int(input())
    heights = [int(input()) for _ in range(n)]
    heights.sort()

    total_dist = 0
    cur_sum = 0
    for h in heights:
        cur_sum += h
        total_dist += 2 * cur_sum

    print(total_dist)

if __name__ == '__main__':
    main()
