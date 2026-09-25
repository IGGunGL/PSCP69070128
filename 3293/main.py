"""Frame"""

lines = []

for i in range(5):
    lines.append(input().rstrip("\r\n"))

max_len = 0
for i in range(5):
    if len(lines[i]) > max_len:
        max_len = len(lines[i])

print("*" * (max_len + 4))

for i in range(5):
    space = max_len - len(lines[i])
    print("* " + lines[i] + (" " * space) + " *")

print("*" * (max_len + 4))
