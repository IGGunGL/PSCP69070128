"""ไข้หวัดกระต่ายสายพันธุ์ใหม่"""

def apply_infection(grid, rows, cols, ir, ic):
    """Apply risk around (ir, ic)"""
    r_min = max(0, ir - 2)
    r_max = min(rows - 1, ir + 2)
    c_min = max(0, ic - 2)
    c_max = min(cols - 1, ic + 2)
    risk_map = {0: 100, 1: 60, 2: 20}
    for r in range(r_min, r_max + 1):
        for c in range(c_min, c_max + 1):
            d = max(abs(r - ir), abs(c - ic))
            risk = risk_map.get(d, 0)
            if risk > grid[r][c]:
                grid[r][c] = risk

def main():
    """main"""
    rows, cols = map(int, input().split())
    rab_r, rab_c = map(int, input().split())
    n = int(input())
    grid = [[0] * cols for _ in range(rows)]
    for _ in range(n):
        ir, ic = map(int, input().split())
        apply_infection(grid, rows, cols, ir, ic)

    safe_count = sum(row.count(0) for row in grid)
    print(safe_count)
    print(f"{grid[rab_r][rab_c]}%")

if __name__ == '__main__':
    main()
