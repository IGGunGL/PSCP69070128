"""GCD"""
import math

n = int(input())
result = 0

for _ in range(n):
    result = math.gcd(result, int(input()))

print(result)
