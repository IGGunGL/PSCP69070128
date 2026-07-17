"""แลกเปลี่ยนเงิน"""
moneywant = int(input())
tens = moneywant // 10
remain = moneywant % 10
five = remain // 5
remain = remain % 5
two = remain // 2
remain = remain % 2
ones = remain
print(f"10 = {tens:.0f}")
print(f"5 = {five:.0f}")
print(f"2 = {two:.0f}")
print(f"1 = {ones:.0f}")
