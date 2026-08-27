"""นวัตกรรมโรงเรียน"""
name = input()
first = ord(name[0].upper())
last = ord(name[-1].upper())
L = len(name)

ans = []
for pos in range(3, 9):
    val = pos - 1
    num = (first + val) if pos % 2 else (last - val)
    rem = num % L
    if rem > 9:
        rem = rem % 10
    ans.append(rem)

print(*ans)
