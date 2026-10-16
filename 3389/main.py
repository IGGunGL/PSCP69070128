"""Smart Trash Collector"""

def main():
    """main"""
    n = int(input())
    for _ in range(n):
        p, c, g = map(float, input().split())
        total = p + c + g
        msgs = [f"{total:.1f}"]
        if total > 50.0:
            msgs.append("Overloaded")
        if p > 20.0:
            msgs.append("Check Type Plastic")
        if c > 20.0:
            msgs.append("Check Type Can")
        if g > 20.0:
            msgs.append("Check Type Glass")
        print(", ".join(msgs))

if __name__ == '__main__':
    main()
