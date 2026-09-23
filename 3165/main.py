"""เดินเล่นในงานเทศกาล"""
moves = input().strip()
x = 0
y = 0
for m in moves:
    if m == 'N':
        y += 1
    elif m == 'S':
        y -= 1
    elif m == 'E':
        x += 1
    elif m == 'W':
        x -= 1

d = abs(x) + abs(y)
print(x, y, d)
