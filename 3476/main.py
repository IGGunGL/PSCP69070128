"""CuteCat CuteFox"""
import json

def main():
    """main"""
    n = int(input())
    cats = {}
    foxes = {}

    for _ in range(n):
        data = json.loads(input())
        for k, v in data.items():
            if k.startswith("Cat") or k.startswith("Fox"):
                code, name = k, v
            else:
                name, code = k, v

            if code.startswith("Cat"):
                cats[code] = name
            elif code.startswith("Fox"):
                foxes[code] = name

    all_names = set(cats.values()) | set(foxes.values())
    if "Cat01" not in cats and "Garfield" not in all_names:
        cats["Cat01"] = "Garfield"
    if "Fox01" not in foxes and "Fubuki" not in all_names:
        foxes["Fox01"] = "Fubuki"

    print(f"Cat : {len(cats)}")
    print(f"Fox : {len(foxes)}")

    for code in sorted(cats, key=lambda c: int(c[3:])):
        print(f"{cats[code]} : {code}")

    for code in sorted(foxes, key=lambda c: int(c[3:])):
        print(f"{foxes[code]} : {code}")

if __name__ == '__main__':
    main()
