"""Bus Seat"""

def main():
    """main"""
    seats_per_row = int(input())
    total_rows = int(input())
    target_seat = int(input())

    for r in range(seats_per_row, 0, -1):
        row_vals = []
        for c in range(1, total_rows + 1):
            seat_num = (c - 1) * seats_per_row + r
            if seat_num == target_seat:
                row_vals.append("XX")
            else:
                row_vals.append(f"{seat_num:02d}")
        print(" ".join(row_vals))
        if r > 1 and not (r - 1) % 2:
            print()

if __name__ == '__main__':
    main()
