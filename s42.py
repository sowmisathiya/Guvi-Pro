cha,che=map(int,input().split())
sha=[]
for p in range(0,cha):
    she=[int(sow) for sow in input().split()]
    sha.append(sorted(she))
for p in range(0,len(sha[0])):
  for q in range(0,len(sha)-1):
    if sha[q][p]>sha[q+1][p]:
      sha[q][p],sha[q+1][p]=sha[q+1][p],sha[q][p]
for p in sha:
  print(*p)
