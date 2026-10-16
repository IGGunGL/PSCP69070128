"""นักสำรวจถ้ำ (Cave Explorer)"""

def main():
    """main"""
    try:
        line = input().strip()
        while not line:
            line = input().strip()
        n = int(line)

        cave_nums = []
        while len(cave_nums) < n:
            row = input().split()
            for val in row:
                cave_nums.append(int(val))

        cmd_line = input().strip()
        while not cmd_line:
            cmd_line = input().strip()
    except (EOFError, ValueError):
        return

    pos = cave_nums.index(1)
    chest_pos = cave_nums.index(2)

    for cmd in cmd_line:
        if cmd in ('L', 'l') and pos > 0:
            pos -= 1
        elif cmd in ('R', 'r') and pos < n - 1:
            pos += 1
        if pos == chest_pos:
            break

    final_cave = [0] * n
    if pos == chest_pos:
        final_cave[pos] = 1
    else:
        final_cave[pos] = 1
        final_cave[chest_pos] = 2

    print(*final_cave)

if __name__ == '__main__':
    main()
