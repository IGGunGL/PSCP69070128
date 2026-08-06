"""ภาษีรถยนต์"""
year = int(input())
cc = int(input())
tax = 0
#เช็กช่วงปี ค.ศ. 1990 หรือเก่ากว่า
if year <= 1990:
    if cc <= 1500:
        tax = 1250
    elif cc <= 2000:
        tax = 1400
    else:
        tax = 2000
#เช็กช่วงปี ค.ศ. 1991 - 1999
elif year <= 1999:
    if cc <= 1500:
        tax = 1100
    elif cc <= 2000:
        tax = 1300
    else:
        tax = 1700
#เช็กช่วงปี ค.ศ. 2000 เป็นต้นมา
else:
    if cc <= 1500:
        tax = 1000
    elif cc <= 2000:
        tax = 1200
    else:
        tax = 1500
print(tax)
