"""Tuple's Sad life"""

def main():
    """main"""
    data = tuple(input().split())
    target = input().strip()

    idx = data.index(target)
    cnt = data.count(target)

    line = " ".join([str(idx)] * cnt)
    for _ in range(cnt):
        print(line)

if __name__ == '__main__':
    main()
