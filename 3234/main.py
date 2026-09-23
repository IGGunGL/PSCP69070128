"""ลำดับสีหลอดไฟประดับต้นคริสต์มาส"""

def main():
    """แสดงลำดับสีหลอดไฟตามจำนวนที่ต้องการ"""
    start_color, count_str = input().split()
    total_bulbs = int(count_str)

    color_names = ["Red", "Green", "Blue"]
    color_keys = ["R", "G", "B"]

    start_index = color_keys.index(start_color.upper())

    result = []
    for i in range(total_bulbs):
        current_index = (start_index + i) % 3
        result.append(color_names[current_index])

    print(" ".join(result))

main()
