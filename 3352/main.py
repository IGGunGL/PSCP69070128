"""LastStand"""
import json

def main():
    """LastStand"""
    data = json.loads(input())
    for x in data:
        print(str(x)[-1])

if __name__ == '__main__':
    main()
