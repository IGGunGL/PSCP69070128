"""AEIOU"""
text = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u']
for i in vowels:
    count = text.count(i)
    if count > 0:
        print(f"{i} : {count}")
