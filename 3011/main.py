"""Color"""
Color1 = input()
Color2 = input()
if Color1 == "Red" and Color2 == "Blue" or Color1 == "Blue" and Color2 == "Red":
    print("Violet")
elif Color1 == "Red" and Color2 == "Yellow" or Color1 == "Yellow" and Color2 == "Red":
    print("Orange")
elif Color1 == "Blue" and Color2 == "Yellow" or Color1 == "Yellow" and Color2 == "Blue":
    print("Green")
elif Color1 == "Red" and Color2 == "Red":
    print("Red")
elif Color1 == "Blue" and Color2 == "Blue":
    print("Blue")
elif Color1 == "Yellow" and Color2 == "Yellow":
    print("Yellow")
elif Color1 == "Red" and Color2 != "Blue" and Color2 != "Yellow":
    print("Error")
elif Color1 == "Blue" and Color2 != "Red" and Color2 != "Yellow":
    print("Error")
elif Color1 == "Yellow" and Color2 != "Red" and Color2 != "Blue":
    print("Error")
else:
    print("Error")
