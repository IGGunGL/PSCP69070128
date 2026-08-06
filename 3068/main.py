"""ปีอธิกสุรทิน"""
year = int(input())

if year < 1582:
    # ยุคเก่าเช็กแค่หาร 4
    if not year % 4:
        print("yes")
    else:
        print("no")
else:
    #ยุคใหม่เช็กตามกฎ
    if not year % 400:
        print("yes")
    elif not year % 100:
        print("no")
    elif not year % 4:
        print("yes")
    else:
        print("no")
