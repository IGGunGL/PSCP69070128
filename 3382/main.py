"""DAY08"""
data_word = []
while True:
    word = input()
    if word == "NULL":
        break
    data_word.append(word)
data_word.reverse()
for i in data_word:
    print(i)
