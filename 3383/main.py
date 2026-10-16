"""Difference"""

def main():
    """main"""
    n = int(input())
    m = int(input())
    set_a = {int(input()) for _ in range(n)}
    set_b = {int(input()) for _ in range(m)}

    diff = sorted(set_a - set_b)
    if diff:
        print(*diff)

if __name__ == '__main__':
    main()
