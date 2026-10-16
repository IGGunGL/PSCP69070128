"""Easy Histogram"""

def main():
    """main"""
    text = input()
    for i in range(26):
        lower = chr(ord('a') + i)
        cnt = text.count(lower)
        if cnt:
            print(f"{lower} = {cnt}")
    for i in range(26):
        upper = chr(ord('A') + i)
        cnt = text.count(upper)
        if cnt:
            print(f"{upper} = {cnt}")

if __name__ == '__main__':
    main()
