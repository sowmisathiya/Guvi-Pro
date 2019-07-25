cha,che=map(int,input().split())
lists=list(map(int,input().split()))
sha=0
for i in range(0,len(lists)):
    if (lists[i]+che)<=5:
        sha+=1
print(sha//3)
