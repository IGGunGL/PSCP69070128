"""รหัสแฝดเทค"""
n = int(input())
code1 = input()
code2 = input()

wrong = 0

for i in range(n):
    total = int(code1[i]) + int(code2[i])

    if total != 9:
        wrong = wrong + 1

if not wrong:
    print("YES")
else:
    print("NO", wrong)
