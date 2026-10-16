"""พูดจาภาษากระต่าย"""


def main():
    """อ่านสตริงแล้วพิมพ์ผลลัพธ์"""
    u = input().strip().upper()
    n = len(u)

    if n > 0 and set(u) <= {"I", "T"}:
        print("unknown", n)
        return

    max_a = 0
    i = 0
    while i < n:
        ch = u[i]
        if ch in "IT":
            i += 1
        elif ch in "RB":
            need = "A" if ch == "R" else "IT"
            j = i + 1
            while j < n and u[j] in need:
                j += 1
            if j == i + 1:
                print("no", j)
                return
            if ch == "R":
                max_a = max(max_a, j - i - 1)
            i = j
        else:
            print("no", i)
            return

    print("yes", max_a)


main()
