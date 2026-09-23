"""ตรวจรางวัลสลากกินแบ่งกระต่ายน้อย"""

def main():
    """คำนวณเงินรางวัลสูงสุดที่กระต่ายน้อยได้รับ"""
    win_char, win_num = input().split()
    my_char, my_num = input().split()

    same_char = win_char == my_char
    same_num = win_num == my_num
    same_last3 = win_num[-3:] == my_num[-3:]
    same_last2 = win_num[-2:] == my_num[-2:]

    if same_char and same_num:
        prize = 1000000
    elif same_num:
        prize = 100000
    elif same_char and same_last3:
        prize = 2000
    elif same_char and same_last2:
        prize = 1000
    elif same_last3:
        prize = 200
    elif same_last2:
        prize = 100
    elif same_char:
        prize = 20
    else:
        prize = 0

    print(prize)

main()
