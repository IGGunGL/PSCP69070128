"""Pad Thai"""

def main():
    """main"""
    required_ings = {
        "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts",
        "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts"
    }
    required_flavs = {"Sweet", "Sour", "Salty"}

    ings = []
    while True:
        item = input().strip()
        if item == "Cook":
            break
        ings.append(item)

    flavs = []
    while True:
        item = input().strip()
        if item == "End":
            break
        flavs.append(item)

    ing_set = set(ings)
    flav_set = set(flavs)

    if not ing_set.issubset(required_ings):
        print("This is not Pad Thai!!!")
    elif ing_set != required_ings:
        print("This is bad!")
    elif flav_set != required_flavs:
        print("Not Bad...")
    else:
        print("Delicious!")

if __name__ == '__main__':
    main()
