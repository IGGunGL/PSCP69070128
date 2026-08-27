"""คำนวณราคาสินค้าโปรโมชั่น"""
pencil , notebook , color = map(int,input().split())
lenall = pencil+notebook+color
price = (pencil*25)+(notebook*40)+(color*55)

if lenall >= 3:
    final_price = price * 0.90
else:
    final_price = price
print(int(final_price))
