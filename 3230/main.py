"""ถอดรหัสเลขห้องโรงแรมกลางกรุง"""

def main():
    """คำนวณเลขห้องจากรหัส 5 หลัก"""
    secret = input().strip().zfill(5)
    d = [int(c) for c in secret]

    floor_codes = ["9", "10", "11", "12", "14"]
    part1 = "13"
    for num, code in zip(d, floor_codes):
        if num > 5:
            part1 = code
            break

    if secret == secret[::-1]:
        part2 = "1" if d[0] + d[4] > 5 else ("2" if d[1] * d[3] > 5 else "0")
    else:
        part2 = "1" if d[4] and (d[0] // d[4]) > 5 else (
            "2" if d[1] - d[4] > 5 else "0"
        )

    prod_val = d[0] * d[1] * d[2] * d[3] * d[4]
    part3 = "1" if sum(d) > 25 else ("2" if prod_val > 55 else "0")

    print(f"{part1}{part2}{part3}")

main()
