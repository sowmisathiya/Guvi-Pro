cha=int(input())
che=list(map(int,input().split()))
sha=0
for i in range(1,len(che)-1):
    if che[i]>che[i-1] and che[i]>che[i+1] or che[i]<che[i-1] and che[i]<che[i+1]:
        sha+=1
if len(che)==1:
    print(1)
else:
    print(sha)
