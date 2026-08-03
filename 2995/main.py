""""ตรวจสอบนักศึกษา"""
idcard = input()
itcard = idcard[2:4] #เช็คตัวที่ 3-4 ว่าเป็น 16 หรือไม่
if itcard == "16":
    print("yes")
else:
    print("no")
