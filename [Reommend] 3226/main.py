"""inflation"""
def main():
    """calculate inflation"""
    n = float(input())
    k = int(input())
    price = int(round(n * 100))
    for _ in range(k):
        price += price * 381 // 10000

    print(f"{price // 100}.{price % 100:02d}")
main()
