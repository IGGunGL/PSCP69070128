"""บุพเพสันนิวาส"""

def main():
    """main"""
    name1 = input().strip()
    name2 = input().strip()

    len1, len2 = len(name1), len(name2)
    if len1 < len2:
        diff = len2 - len1
        pad = "".join(name1[i % len1] for i in range(diff))
        name1 += pad
    elif len2 < len1:
        diff = len1 - len2
        pad = "".join(name2[i % len2] for i in range(diff))
        name2 += pad

    love = set("loveLOVE")
    result = []
    for c1, c2 in zip(name1, name2):
        if c1 in love or c2 in love:
            result.append("w")
        else:
            result.append("$")

    s = "".join(result)
    w_count = s.count("w")

    if w_count % 2:
        max_run = 0
        cur_run = 0
        for ch in s:
            if ch == 'w':
                cur_run += 1
                max_run = max(max_run, cur_run)
            else:
                cur_run = 0
        s += str(max_run)
    else:
        if "ww" not in s:
            s += "#"

    print(s)

if __name__ == '__main__':
    main()
