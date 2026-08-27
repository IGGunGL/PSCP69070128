"""พอด"""
n, k = map(int, input().split())
counts = [0] * (k + 1)
for _ in range(n):
    line = int(input())
    counts[line] += 1
min_pods = min(counts[1:])
remaining = n - (min_pods * k)
print(remaining)
