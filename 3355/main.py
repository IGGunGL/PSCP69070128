"""Shorten"""

def main():
    """main"""
    nums = []
    while True:
        val = int(input())
        if val == -1:
            break
        nums.append(val)

    if not nums:
        return

    ranges = []
    start = nums[0]
    prev = nums[0]

    for x in nums[1:]:
        if x == prev + 1:
            prev = x
        else:
            if start == prev:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{prev}")
            start = x
            prev = x

    if start == prev:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}-{prev}")

    print(", ".join(ranges))

if __name__ == '__main__':
    main()
