"""ผลรวมของค่ามากกว่า"""
N = int(input())

NUMS = []
for _ in range(N):
    A = int(input())
    B = int(input())
    NUMS.append(max(A, B))

if N == 1:
    print(NUMS[0])
else:
    EQUATION = " + ".join(map(str, NUMS))
    TOTAL = sum(NUMS)
    print(f"{EQUATION} = {TOTAL}")
