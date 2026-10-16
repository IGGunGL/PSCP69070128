"""Array ฮาเฮ"""

def main():
    """main"""
    nums = []
    for i in range(1, 4):
        val = int(input())
        nums.append(val)
        print(f"Input number {i} stored.")

    while True:
        menu = int(input())
        if not menu:
            break
        if menu == 1:
            print("Original order:", *nums)
        elif menu == 2:
            print("Descending order:", *sorted(nums, reverse=True))
        elif menu == 3:
            print("Ascending order:", *sorted(nums))

if __name__ == '__main__':
    main()
