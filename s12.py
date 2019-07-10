from itertools import combinations
cho,che= input().split()
che=int(che)
sha=[]
hue= combinations(cho,len(cho)-che)
for p in hue:
    sha.append("".join(p))
print(min(sha))
