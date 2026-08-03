"""ใส่หมายเลขไปปุ้บจะกลับตัวเลขและบวกหรือคูณกับตัวเลขกลับด้าน"""
def main():
    """GL"""
    number = int(input())
    symbol = input()
    number_reversed = int(str(number)[::-1])
    ans = 0
    if symbol == '+':
        ans = number + int(number_reversed)
    elif symbol == '*':
        ans = number * int(number_reversed)
    print(f'{number} {symbol} {number_reversed} = {ans}')
main()
