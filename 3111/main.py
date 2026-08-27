"""สหกรณ์"""
from decimal import Decimal, ROUND_HALF_UP

is_member = input().strip().upper()
n = int(input().strip())

total = Decimal('0.00')
for _ in range(n):
    total += Decimal(input().strip())

if is_member == 'Y':
    net_total = total * Decimal('0.95')
elif is_member == 'N' and total >= Decimal('500'):
    net_total = total * Decimal('0.97')
else:
    net_total = total

result = net_total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(f"{result:.2f}")
