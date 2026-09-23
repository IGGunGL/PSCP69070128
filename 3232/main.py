"""กบน้อยกระโดด"""

def main():
    """คำนวณจำนวนครั้งขั้นต่ำในการกระโดดให้ถึงระยะ Y"""
    x, y = map(int, input().split())

    current_dist = x
    total_dist = 0
    jumps = 0

    while current_dist > 0:
        total_dist += current_dist
        jumps += 1

        if total_dist >= y:
            print(jumps)
            return

        current_dist -= 2

    print(-1)

main()
