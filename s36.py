tat=int(input())
sosa=list(map(int,input().split()))
caa=[]
naa=1
for i in sosa:
  if i not in caa:
    caa.append(i)
for i in range(0,len(caa)-1):
  if caa[i]<caa[i+1]:
    naa+=1
print(naa)
