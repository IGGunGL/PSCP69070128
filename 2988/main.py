"""ตรวจสอบบัตรประชาชน"""
idcard = input()
if len(idcard) == 13 and idcard.isdigit(): #isdigit() เช็คว่าตัวเลขทั้งหมดมั้ย
    print("yes")
else:
    print("no")
