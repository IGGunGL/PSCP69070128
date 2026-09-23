"""ขโมย"""
n, k, t = map(int, input().split())

pos = 1
count = 1

if t == 1:
    print(1)
else:
    while True:
        pos = (pos - 1 + k) % n + 1
        if pos == 1:
            break
        count += 1
        if pos == t:
            break
    print(count)
