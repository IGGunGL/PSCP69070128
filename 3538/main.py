"""B - Fully pair?"""

def main():
    """main"""
    text = input().strip()
    counts = {}
    order = []
    for char in text:
        if char not in counts:
            counts[char] = 0
            order.append(char)
        counts[char] += 1

    unpaired = []
    for char in order:
        if counts[char] % 2:
            unpaired.append(char)

    if not unpaired:
        print("fully paired")
    else:
        print("".join(unpaired))

if __name__ == '__main__':
    main()
