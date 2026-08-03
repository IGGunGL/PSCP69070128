"""ตรวจสอบตำแหน่งพิกัด (X, Y)"""
def main():
    """ตรวจสอบตำแหน่งพิกัด (X, Y)"""
    x = int(input())
    y = int(input())
    if x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y < 0:
        print("Q3")
    elif x < 0 < y:
        print("Q2")
    elif x > 0 > y:
        print("Q4")
    elif not x and y:
        print("Y")
    elif x and not y:
        print("X")
    else:
        print("O")
main()
