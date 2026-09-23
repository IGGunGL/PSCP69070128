"""ยอดร้าน"""
day = int(input())
total = []
for _ in range(day):
    oneday = int(input())
    total.append(oneday)
print(sum(total))
print(max(total))
print(min(total))
print(f'{sum(total) / len(total):.1f}')
