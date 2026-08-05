"""ปีอธิกสุรทิน"""
year = int(input())

if year < 1582:
    # ยุคเก่า: เช็กแค่หาร 4
    if not year % 4:
        print("yes")
    else:
        print("no")
else:
    # ยุคใหม่: เช็กตามกฎ 400 -> 100 -> 4
    if not year % 400:
        print("yes")
    elif not year % 100:
        print("no")
    elif not year % 4:
        print("yes")
    else:
        print("no")
