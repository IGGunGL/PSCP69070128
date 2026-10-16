"""Muddled Menu"""

def main():
    """main"""
    menu = []
    while True:
        line = input().strip()
        if line == "DONE":
            break
        if line == "CLOSED":
            menu = []
            break
        if line == "SOMETHING'S WRONG":
            menu = []
        elif line.startswith("Can't do: "):
            item = line[10:]
            if item in menu:
                menu.remove(item)
        elif " #" in line:
            parts = line.rsplit(" #", 1)
            item = parts[0]
            if parts[1] == "N":
                menu.append(item)
            else:
                pos = int(parts[1]) - 1
                menu.insert(pos, item)

    print("Full Course:", menu, "Reversed:", menu[::-1])

if __name__ == '__main__':
    main()
