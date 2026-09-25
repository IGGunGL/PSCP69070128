"""RGB Mixer"""
r1, g1, b1 = map(int, input().split())
r2, g2, b2 = map(int, input().split())

new_r = (r1 + r2) // 2
new_g = (g1 + g2) // 2
new_b = (b1 + b2) // 2

print(new_r, new_g, new_b)
