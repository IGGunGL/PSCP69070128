"""ผ่านไม่ผ่าน"""
midterm = int(input())
final = int(input())
scoresum = midterm + final
print(scoresum)
if scoresum >= 50:
    print("pass")
else:
    print("fail")
