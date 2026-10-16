"""ส่งต่อ"""

def main():
    """main"""
    n, s = map(int, input().split())
    next_p = [0] * (n + 1)
    for i in range(1, n + 1):
        next_p[i] = int(input().strip())

    visited = set()
    curr = s
    while curr and curr not in visited:
        visited.add(curr)
        curr = next_p[curr]

    print(len(visited))

if __name__ == '__main__':
    main()
