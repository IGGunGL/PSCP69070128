"""coke"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if not d:
    print(0)
elif not b:
    print(d * a)
else:
    discounted_bottles = (d - 1) // b
    full_price_bottles = d - discounted_bottles
    total_cost = (full_price_bottles * a) + (discounted_bottles * c)
    print(total_cost)
