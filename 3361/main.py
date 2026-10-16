"""ขายรถยนต์"""

def main():
    """main"""
    n = int(input())
    v_list = []
    for _ in range(n):
        _, v = map(int, input().split())
        v_list.append(v)

    unsold = 0
    max_v = -1
    for v in v_list[::-1]:
        if v < max_v:
            unsold += 1
        else:
            max_v = v

    print(unsold)

if __name__ == '__main__':
    main()
