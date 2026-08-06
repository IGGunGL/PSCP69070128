"""อยากเป็นsaitama"""
import math
pushup = int(input())
situp = int(input())
looksit = int(input())
run = int(input())
canpush = int(input())
cansit = int(input())
canrun = int(input())
canlook = int(input())

pushupsum = pushup/canpush
situpsum = situp/cansit
looksitsum = looksit/canlook
runsum = run/canrun

print(math.ceil(max(pushupsum,situpsum,runsum,looksitsum)))
