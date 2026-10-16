"""Resistor"""

def main():
    """main"""
    digits = {
        "Black": 0, "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4,
        "Green": 5, "Blue": 6, "Purple": 7, "Grey": 8, "White": 9
    }
    multipliers = {
        "Black": 1, "Brown": 10, "Red": 100, "Orange": 1000, "Yellow": 10000,
        "Green": 100000, "Blue": 1000000, "Purple": 10000000,
        "Gold": 0.1, "Silver": 0.01
    }
    tolerances = {
        "Brown": 1, "Red": 2, "Green": 0.5, "Blue": 0.25, "Purple": 0.10,
        "Grey": 0.05, "Gold": 5, "Silver": 10
    }

    c1 = input().strip()
    c2 = input().strip()
    c3 = input().strip()
    c4 = input().strip()

    if c1 not in digits or c2 not in digits or c3 not in multipliers or c4 not in tolerances:
        print("Error")
        return

    base = (digits[c1] * 10 + digits[c2]) * multipliers[c3]
    tol = tolerances[c4]
    lower = base * (1 - tol / 100)
    upper = base * (1 + tol / 100)
    print(f"{lower:.4f}")
    print(f"{upper:.4f}")

if __name__ == '__main__':
    main()
