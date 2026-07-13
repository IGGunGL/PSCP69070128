"""GL"""
def main():
    """GL"""
    var = (input()).split()
    width = int(var[0])
    length = int(var[1])
    height = int(var[2])
    area = (width*2+length*2)*height
    price = int(input())
    ans = area*price
    print(area)
    print(ans)
main()
