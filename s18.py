import math
cha,cho=map(int,input().split())
oho=[]
gaa=list(map(int,input().split()))
for p in range(0,cho):
    love,hut=map(int,input().split())
    oho.append([love,hut])
for p in oho:
    kaa=p[0]-1
    laa=p[1]-1
    print(math.gcd(gaa[kaa],gaa[laa]))
