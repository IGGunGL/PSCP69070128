"""Rabbit"""
rabbit = int(input())
all_scores = []
while rabbit > 0:
    score = int(input())
    all_scores.append(score)
    rabbit -= 1
top_score = max(all_scores)
count_top = all_scores.count(top_score)
print(f"{top_score}")
print(f"{count_top}")
