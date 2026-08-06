"""cal"""
def main():
    """cal"""
    num = int(input())
    symbol = num
    press = 0
    if num == 1:
        print(1)
    else:
        for _ in range(num):
            press += len(str(num))
            num -= 1
        print(press+symbol)
main()
