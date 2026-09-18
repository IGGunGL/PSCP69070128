"""ElectricUsing"""
nuay = int(input())
money = 0
if nuay <= 10:
    money = nuay * 5
elif nuay <= 50:
    money = +50 + (nuay - 10) * 7
elif nuay <= 100:
    money = 50 + 280 + (nuay - 50) * 10
elif nuay <= 200:
    money = 50 + 280 + 500 + (nuay - 100) * 12
else:
    money = 50 + 280 + 500 + 1200 + (nuay - 200) * 15
allmoney = money * 100
ft = nuay * 50
vat = money * 7
sumary = allmoney + ft + vat

padset = (sumary + 5) // 10
bath = padset // 10
satang = padset % 10

print(f"{bath}.{satang}")
