"""testlist"""
numbers = [4, 8, 15, 16, 23, 42]

total = 0
minnum = numbers[0]
maxnum = numbers[0]

for i in numbers:
    total += i
    
    if i > maxnum:
        maxnum = i
        
    if i < minnum:
        minnum = i

print("ผลรวม:", total)
print("ค่าน้อยสุด:", minnum)
print("ค่ามากสุด:", maxnum)