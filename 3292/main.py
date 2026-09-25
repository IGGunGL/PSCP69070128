"""Arrow"""
character = input()
num = int(input())

def right_arrow():
    """right_arrow"""
    space = 0
    for i in range(num):
        print(" " * space + "*" * (num - i))
        space += 2
    space -= 2
    for i in range(2,num + 1):
        space -= 2
        print(" " * space + "*" * (i))
def left_arrow():
    """left_arrow"""
    space = num - 1
    for i in range(num):
        print(" " * space + "*" * (num - i))
        space -= 1
    space = 0
    for i in range(2,num + 1):
        space += 1
        print(" " * space + "*" * (i))

for pos, alphabet in enumerate(character):
    if alphabet == "R":
        right_arrow()
    elif alphabet == "L":
        left_arrow()
    if pos < len(character) - 1:
        print()
