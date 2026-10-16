"""WordSequence I"""

def main():
    """main"""
    text = input().strip()
    for i in range(1, len(text) + 1):
        print(text[:i])

if __name__ == '__main__':
    main()
