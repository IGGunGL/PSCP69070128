p = float(input())
t = int(input())

for _ in range(t):
    increase = p * 0.0381
    increase = int(increase * 100) / 100
    p += increase
print(f"{p:.2f}")
