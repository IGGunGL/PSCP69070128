"""Pig"""

def main():
    """main"""
    n = int(input())
    weights = list(map(int, input().split()))

    max_weights = []
    for i in range(n):
        w1 = weights[2 * i]
        w2 = weights[2 * i + 1]
        max_weights.append(max(w1, w2))

    if n == 1:
        print(max_weights[0])
    else:
        eq = " + ".join(map(str, max_weights))
        print(f"{eq} = {sum(max_weights)}")

if __name__ == '__main__':
    main()
