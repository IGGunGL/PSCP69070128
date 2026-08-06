"""หาค่าน้อยสุดโดยบรรทัดแรกใส่ว่าจะเอากี่ตัว"""
n = int(input())
low_value = float('inf')

for i in range(n):
    num = int(input())
    if num < low_value:
        low_value = num
    i=i-0
print(low_value)
