"""Pickthemagain"""
def main():
    """โปรแกรมหาตัวเลขที่ตรงเงื่อนไข"""
    text = input().split()
    ans = []

    for x in text:
        num = int(x)
        if not num % 3 or not num % 5:
            ans.append(num)

    if not ans:
        print("Nope")
    else:
        for num in ans[::-1]:
            print(num)

main()
