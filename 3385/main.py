"""BusStop I"""

def main():
    """main"""
    p = int(input())
    n = int(input())

    stops = {}
    for _ in range(n):
        parts = list(map(int, input().split()))
        stops[parts[0]] = parts[1:]

    on_bus = []
    alighted_count = 0

    for s in range(1, n + 1):
        remaining_on_bus = []
        for dest in on_bus:
            if dest == s:
                alighted_count += 1
            else:
                remaining_on_bus.append(dest)
        on_bus = remaining_on_bus

        waiting = stops.get(s, [])
        for dest in waiting:
            if len(on_bus) >= p:
                break
            if dest > s:
                on_bus.append(dest)

    print(alighted_count)

if __name__ == '__main__':
    main()
