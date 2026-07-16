"""Bill"""
price = float(input())
pricecharge = price * 0.10
if pricecharge > 1000:
    pricecharge = 1000
elif not pricecharge:
    pricecharge = 0
elif pricecharge < 50:
    pricecharge = 50
pricesumcharge = price + pricecharge
pricevat = pricesumcharge * 1.07
print(f'{pricevat:.2f}')
