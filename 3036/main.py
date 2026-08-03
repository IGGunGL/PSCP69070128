"""Pyramid Treasure Room"""
import math


def main():
    """Main Function"""
    n_room = int(input())

    # 1. หาเลขชั้น r (1, 2, 3, ...)
    if n_room == 1:
        r = 1
    else:
        r = math.isqrt(n_room - 1) + 1

    # 2. หาลำดับห้อง k ในชั้นนั้น (1 ถึง 2r - 1)
    k = n_room - (r - 1) ** 2

    # 3. คำนวณจำนวนกำแพงตามทิศทางสามเหลี่ยม (k คี่ = ชี้ขึ้น, k คู่ = ชี้ลง)
    if k % 2 == 1:
        walls = 2 * (r - 1)
    else:
        walls = 2 * (r - 1) - 1

    print(walls)


if __name__ == "__main__":
    main()