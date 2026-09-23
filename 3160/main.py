"""จำนวนเฉพาะ"""
start, end = map(int, input().split())

if start > end:
    start, end = end, start

primes = []

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if not num % i:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

if primes:
    print(*primes)
print(f"Total primes: {len(primes)}")
