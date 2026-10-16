"""นก"""

def main():
    """main"""
    n = int(input())
    heights = list(map(int, input().split()))

    if n <= 1:
        print(n)
        return

    count = 0
    for i in range(n):
        if not i:
            if heights[0] > heights[1]:
                count += 1
        elif i == n - 1:
            if heights[n - 1] > heights[n - 2]:
                count += 1
        else:
            if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
