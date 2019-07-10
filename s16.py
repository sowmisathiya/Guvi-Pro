cha=int(input())
sha=list(map(int,input().split()))
h=0
for g in range(len(sha)-2):
    for p in range(g+1,len(sha)-1):
        for love in range(p+1,len(sha)):
            if sha[g]<sha[p]<sha[love] and g<p<love:
                h=h+1
print(h)
