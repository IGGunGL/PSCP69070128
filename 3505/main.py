"""PickNum"""

def main():
    """main"""
    nums = list(map(int, input().split()))
    pos = sum(1 for x in nums if x > 0)
    neg = sum(1 for x in nums if x < 0)
    zero = sum(1 for x in nums if x == 0)
    print(f"Positive: {pos}")
    print(f"Negative: {neg}")
    print(f"Zero: {zero}")

if __name__ == '__main__':
    main()
