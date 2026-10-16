"""หุ่นยนต์เคาะเสียงกระเบื้อง"""

def main():
    """main"""
    parts = input().split()
    n = int(parts[0])
    p = float(parts[1])

    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    for r in range(n):
        def_tiles = sum(1 for x in grid[r] if x > 0)
        tot_pts = sum(grid[r])
        print(*(grid[r] + [def_tiles, tot_pts]))

    col_def = [sum(1 for r in range(n) if grid[r][c] > 0) for c in range(n)]
    print(*col_def)

    col_pts = [sum(grid[r][c] for r in range(n)) for c in range(n)]
    print(*col_pts)

    total_def_tiles = sum(col_def)
    total_def_pts = sum(col_pts)
    fine = total_def_pts * p
    print(f"{total_def_tiles} {total_def_pts} {fine:.2f}")

if __name__ == '__main__':
    main()
