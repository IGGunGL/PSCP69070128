"""กระต่ายกินราเมน"""
size, r_type = input().split()

price = 0
if size == 'S':
    price = 60 if r_type == 'R' else 80
elif size == 'M':
    price = 80 if r_type == 'R' else 100
elif size == 'L':
    price = 100 if r_type == 'R' else 120

topping_input = input().split()
topping = topping_input[0]

if topping == 'P':
    qty = int(topping_input[1])
    price += qty * 15
elif topping == 'E':
    qty = int(topping_input[1])
    price += qty * 10

print(price)
