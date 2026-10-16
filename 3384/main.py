"""PickThem"""
import json

def main():
    """main"""
    data = json.loads(input())
    evens = [x for x in data if not x % 2]
    if evens:
        for x in evens:
            print(x)
    else:
        print("Nope")

if __name__ == '__main__':
    main()
