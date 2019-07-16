aaa=int(input())
raa=list(map(int,input().split()))
raa.sort(reverse=True)
saa=0
sho=0
resu=[]
for p in range(0,aaa,2):
    saa=saa+raa[p]
for q in range(1,aaa,2):
    sho=sho+raa[q]
resu.append([saa,sho])
for p in resu:
    print(p[0] if p[0]>p[1] else p[1])
