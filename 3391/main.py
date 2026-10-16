"""สะสมเหรียญเวทย์มนตร์"""

def main():
    """main"""
    n = int(input())
    total_f = 0
    total_w = 0
    total_e = 0
    for _ in range(n):
        f1, w1, e1, f2, w2, e2 = map(int, input().split())
        total_f += max(f1, f2)
        total_w += max(w1, w2)
        total_e += max(e1, e2)

    total = total_f + total_w + total_e
    bonus = "YES" if total_f > (total_w + total_e) else "NO"
    print(f"Total: {total}")
    print(f"Fire: {total_f}")
    print(f"Water: {total_w}")
    print(f"Earth: {total_e}")
    print(f"Bonus: {bonus}")

if __name__ == '__main__':
    main()
