"""Conan"""
text = input()
shift = int(input()) % 26

ans = ""
for char in text:
    num = ord(char) - ord('a')
    new_num = (num + shift) % 26
    ans += chr(new_num + ord('a'))
print(ans)
