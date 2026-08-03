"""Surprisevote"""
allvote = float(input())
bestvote = float(input())
total = allvote - (2 * bestvote)
if total < 0:
    total = 0

if bestvote - total > 2:
    print("Surprising")
else:
    print("Not surprising")
