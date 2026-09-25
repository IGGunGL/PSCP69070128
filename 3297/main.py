"""Movie Ticket"""

def main():
    """การซื้อตั๋ว"""
    total_seats = int(input())

    while total_seats > 0:
        try:
            line = input().strip()
            if not line:
                continue

            parts = line.split()
            age = int(parts[0])
            tickets = int(parts[1])

            if age < 15:
                print(-1)
            elif tickets > total_seats:
                print(-2)
            else:
                if 15 <= age <= 22:
                    price = 120
                elif age >= 60:
                    price = 75
                else:
                    price = 150

                total_price = price * tickets
                total_seats -= tickets
                print(f"{total_price} {total_seats}")

        except EOFError:
            break

main()
