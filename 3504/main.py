"""Hamming"""

def main():
    """main"""
    s1 = input().strip()
    s2 = input().strip()
    dist = sum(1 for c1, c2 in zip(s1, s2) if c1 != c2)
    print(dist)

if __name__ == '__main__':
    main()
