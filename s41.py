cha,che=input().split()
sha=abs(len(cha)-len(che))
for i in range(len(cha)):
  if len(che)==1 and che[i] in cha:
   break
  if cha[i]!=che[i]:
   sha+=1
print(sha)
