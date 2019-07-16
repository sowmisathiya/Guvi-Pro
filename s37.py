sha,kaa=map(int,input().split())
psa=list(map(int,input().split()))
vsa=list(map(int,input().split()))
tsa=[]
cina=0
for i in range(sha):
    xaa=vsa[i]/psa[i]
    tsa.append(xaa)
while kaa>=0 and len(tsa)>0:
    mindexa=tsa.index(max(tsa))
    if kaa>=psa[mindexa]:
        cina=cina+vsa[mindexa]
        kaa=kaa-psa[mindexa]
    psa.pop(mindexa)
    vsa.pop(mindexa)
    tsa.pop(mindexa)
print(cina)
