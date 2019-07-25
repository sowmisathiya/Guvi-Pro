cha=input()
che=list(map(int,input().split()))
sha=0
for i in range(0,len(che)-2):
    for j in range(i+1,len(che)-1):
        for k in range(j+1,len(che)):
            if che[i]>che[j] and che[j]>che[k]:
                sha+=1
print(sha)
