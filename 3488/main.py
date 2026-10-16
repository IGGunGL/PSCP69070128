"""ไฟส่อง"""

def main():
    """main"""
    n = int(input())
    lit = [False] * 360
    for _ in range(n):
        a, b = map(int, input().split())
        if a < b:
            for d in range(a, b):
                lit[d] = True
        else:
            for d in range(a, 360):
                lit[d] = True
            for d in range(0, b):
                lit[d] = True

    if all(lit):
        print(360)
        return

    lit2 = lit + lit
    max_run = 0
    cur_run = 0
    for is_l in lit2:
        if is_l:
            cur_run += 1
            max_run = max(max_run, cur_run)
        else:
            cur_run = 0

    print(min(max_run, 360))

if __name__ == '__main__':
    main()
