"""ส่งของ"""
origin, dest = input().split()
weight = float(input())

if origin == "BKK" and dest == "CNX":
    print(f"{10 + weight * 30:.2f}")
elif origin == "CNX" and dest == "UBP":
    print(f"{15 + weight * 40:.2f}")
elif origin == "UBP" and dest == "BKK":
    print(f"{20 + weight * 40:.2f}")
elif origin == "BKK" and dest == "PKT":
    print(f"{25 + weight * 50:.2f}")
elif origin == "PKT" and dest == "CNX":
    print(f"{30 + weight * 60:.2f}")
elif origin == "UBP" and dest == "PKT":
    print(f"{40 + weight * 70:.2f}")
else:
    print("Error")
"""ส่งของ"""
origin, dest = input().split()
weight = float(input())

if origin == "BKK" and dest == "CNX":
    print(f"{10 + weight * 30:.2f}")
elif origin == "CNX" and dest == "UBP":
    print(f"{15 + weight * 40:.2f}")
elif origin == "UBP" and dest == "BKK":
    print(f"{20 + weight * 40:.2f}")
elif origin == "BKK" and dest == "PKT":
    print(f"{25 + weight * 50:.2f}")
elif origin == "PKT" and dest == "CNX":
    print(f"{30 + weight * 60:.2f}")
elif origin == "UBP" and dest == "PKT":
    print(f"{40 + weight * 70:.2f}")
else:
    print("Error")
