paa=int(input())
naa=list(map(int,input().split()))
naa.sort()
saa=0
sva=0
for i in range(len(naa)):
    if naa[i]>=saa:
        sva=sva+1
    saa=saa+naa[i]
print(sva)
