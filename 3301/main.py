"""Best Box Size"""

def main():
    """คำนวณหาพื้นที่เหลือที่น้อยที่สุด"""
    line = input().split()
    if not line:
        return

    w = int(line[0])
    l = int(line[1])
    m = int(line[2])
    n = int(line[3])

    total_area = w * l
    min_waste = total_area

    for a in range(m, n + 1):
        horiz_boxes = (w // a) * l
        rem_w = w % a

        vert_boxes = (l // a) * rem_w

        used_area = (horiz_boxes + vert_boxes) * a
        waste = total_area - used_area

        if waste < min_waste:
            min_waste = waste

        if not min_waste:
            break

    print(min_waste)

main()
