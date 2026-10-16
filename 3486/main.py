"""ตำบลกระสุนตก"""

def find_target(reports):
    """Find target coordinates"""
    x1, y1, d1 = reports[0]
    for dx in range(-d1, d1 + 1):
        rem = d1 * d1 - dx * dx
        dy = int(rem ** 0.5)
        if dy * dy == rem:
            signs = [1, -1] if dy else [1]
            for sign in signs:
                tx, ty = x1 + dx, y1 + sign * dy
                if all((tx - xi) ** 2 + (ty - yi) ** 2 == di * di for xi, yi, di in reports[1:]):
                    return tx, ty
    return None

def main():
    """main"""
    n = int(input())
    reports = [tuple(map(int, input().split())) for _ in range(n)]
    ans = find_target(reports)
    if ans:
        print(f"{ans[0]} {ans[1]}")

if __name__ == '__main__':
    main()
