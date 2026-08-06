"""ฟีลเตอร์ AR Tiktok"""
r, x, y = map(int, input().split())
if x*x + y*y < r*r:
    print("IN")
elif x*x + y*y == r*r:
    print("ON")
else:
    print("OUT")
