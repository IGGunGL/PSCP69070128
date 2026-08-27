"""AOT"""
num, check = map(int, input().split())
check = check+0

diff = [0] * 1442

for _ in range(num):
    start, stop = map(int, input().split())
    diff[start] += 1
    diff[stop] -= 1

active_stores = [0] * 1441
current = 0
for t in range(1441):
    current += diff[t]
    active_stores[t] = current

queries = list(map(int, input().split()))

results = [str(active_stores[k]) for k in queries]
print(' '.join(results))
