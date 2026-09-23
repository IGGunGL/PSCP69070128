"""วาด X-shape สไตล์ Elon Musk"""

def main():
    """วาด X-shape"""
    text = input()

    k = text[-1]
    size = int(text[:-1])

    mid = size // 2

    for r in range(size):
        line = ""

        if k == "#":
            char = "#"
        else:
            dist = abs(r - mid)
            char = chr(ord(k) + dist)

        for c in range(size):
            if c in (r, size - 1 - r):
                line = line + char
            else:
                line = line + "-"

        print(line)

main()
