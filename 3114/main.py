"""Suvarnabhumi"""
import math

h_in, m_in = map(int, input().split('.'))
h_out, m_out = map(int, input().split('.'))

if not (0 <= h_in <= 23 and 0 <= m_in <= 59 and 0 <= h_out <= 23 and 0 <= m_out <= 59):
    print("ERROR")
else:
    time_in = h_in * 60 + m_in
    time_out = h_out * 60 + m_out
    diff = time_out - time_in

    if diff < 0 or diff > 1440:
        print("ERROR")
    elif diff <= 15:
        print("FREE")
    else:
        # ปัดเศษนาทีขึ้นเป็น 1 ชม.
        hours = math.ceil(diff / 60)

        if hours == 1:
            print(25)
        elif hours == 2:
            print(50)
        elif hours == 3:
            print(80)
        elif hours == 4:
            print(110)
        elif hours == 5:
            print(145)
        elif hours == 6:
            print(180)
        elif 7 <= hours <= 24:
            print(250)
        else:
            print("ERROR")
