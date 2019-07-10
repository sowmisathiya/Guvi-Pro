cha,che=map(int,input().split())
kaa=[]
shu=[]
sha=[int(p) for p in input().split() ]
for g in range(0,che):
    usa,un=map(int,input().split())
    for h in range(usa-1 ,un):
        shu.append(sha[h])
    xaa=sorted(shu)
    kaa.append(min(shu))
    del shu[:]
for o in range(0,len(kaa)):
    print(kaa[o])
