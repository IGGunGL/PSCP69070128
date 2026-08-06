"""นับสระ"""
select = int(input())
Vowel = ["A", "E", "I", "O", "U"]
count = 0
for i in range(select):
    Letter = input().upper()
    if Letter in Vowel:
        count += 1
        i=i-0
print(count)
