"""สินค้าส่งออก"""
n = int(input())
total = 0
even = 0
odd = 0
for _ in range(n):
    x = int(input())
    total += x
    if not x % 2:
        even += 1
    else:
        odd += 1

print("SUM", total)
print("EVEN", even)
print("ODD", odd)
