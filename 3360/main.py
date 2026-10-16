"""หั่นขนมปัง"""

def main():
    """main"""
    w, h, *_ = map(int, input().split())
    x_cuts = list(map(int, input().split()))
    y_cuts = list(map(int, input().split()))

    all_x = [0] + x_cuts + [w]
    all_y = [0] + y_cuts + [h]

    widths = [all_x[i] - all_x[i-1] for i in range(1, len(all_x))]
    heights = [all_y[i] - all_y[i-1] for i in range(1, len(all_y))]

    widths.sort(reverse=True)
    heights.sort(reverse=True)

    max1 = widths[0] * heights[0]
    cand1 = widths[0] * heights[1] if len(heights) > 1 else 0
    cand2 = widths[1] * heights[0] if len(widths) > 1 else 0
    max2 = max(cand1, cand2)

    print(f"{max1} {max2}")

if __name__ == '__main__':
    main()
