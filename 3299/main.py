"""สวน"""
def main():
    """นับช่อง"""
    line = input().split()
    if not line:
        return
    l = int(line[0])
    n = int(line[1])

    current_band_size = l * (l + 1) // 2
    band = 1

    while n > current_band_size:
        n -= current_band_size
        band += 1
        current_band_size += l * l

    print(band)

main()
