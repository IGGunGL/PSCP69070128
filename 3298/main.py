"""Rabbit at BUU"""

def main():
    """ตรวจข้อความ"""
    text = input().strip()
    upper = text.upper()

    max_u = 0
    for i, ch in enumerate(upper):
        if ch == 'B':
            k = i + 1
            while k < len(upper) and upper[k] == 'U':
                k += 1
            max_u = max(max_u, k - (i + 1))

    if max_u >= 2:
        print(f"Yes {max_u}")
    elif 'B' in upper:
        pos = upper.index('B')
        print(text[:pos + 1] + 'U' * (len(text) - pos - 1))
    else:
        print(('BUU' * len(text))[:len(text)])

main()
