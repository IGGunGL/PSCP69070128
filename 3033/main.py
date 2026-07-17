"""กระดาษห่อของขวัญ"""
num = input().split()
radius = float(num[0])
height = float(num[1])
glue = float(num[2])
width = height + (2*radius)
length = (2 * 3.14 * radius) + glue
print(f"{width:.2f} {length:.2f}")
