"""GL"""
import math
def main():
    """GL"""
    var1 = (input()).split()
    var2 = (input()).split()
    x1 = int(var1[0])
    y1 = int(var1[1])
    z1 = int(var1[2])
    x2 = int(var2[0])
    y2 = int(var2[1])
    z2 = int(var2[2])
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f'{d:.2f}')
main()
