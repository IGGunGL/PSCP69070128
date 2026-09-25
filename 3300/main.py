"""Work-Life Balance"""
def main():
    """คำนวณจำนวนวันน้อยที่สุดที่ต้องใช้ทำงานทั้งหมด"""
    n = int(input())

    tasks = []
    while len(tasks) < n:
        tasks.extend(map(int, input().split()))

    heavy_tasks = 0
    for h in tasks:
        if h > 18:
            heavy_tasks += 1

    ans = max(n, 2 * heavy_tasks - 1)
    print(ans)

main()
