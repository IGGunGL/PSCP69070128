"""Array 2D ตรวจสอบ"""

def main():
    """main"""
    grid = [list(map(int, input().split())) for _ in range(5)]

    odd_row = -1
    for r in range(5):
        if sum(grid[r]) % 2:
            odd_row = r
            break

    odd_col = -1
    for c in range(5):
        col_sum = sum(grid[r][c] for r in range(5))
        if col_sum % 2:
            odd_col = c
            break

    if odd_row != -1 and odd_col != -1:
        print(f"{odd_row} {odd_col}")
    else:
        print("-1 -1")

if __name__ == '__main__':
    main()
