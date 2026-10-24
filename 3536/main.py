"""isPrime_large"""

def is_prime(num):
    """check if num is prime"""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if not num % 2 or not num % 3:
        return False
    i = 5
    while i * i <= num:
        if not num % i or not num % (i + 2):
            return False
        i += 6
    return True

def main():
    """main"""
    n = int(input())
    if is_prime(n):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
