"""FourDirections"""

def main():
    """main"""
    dirs = input().strip()
    arrows = {
        'U': ["  *  ", " *** ", "* * *", "  *  ", "  *  "],
        'D': ["  *  ", "  *  ", "* * *", " *** ", "  *  "],
        'L': ["  *  ", " *   ", "*****", " *   ", "  *  "],
        'R': ["  *  ", "   * ", "*****", "   * ", "  *  "],
    }
    for r in range(4):
        print("".join(arrows[x][r] + " " for x in dirs))
    print("".join(arrows[x][4] + " " for x in dirs).rstrip() + " ")

if __name__ == '__main__':
    main()
