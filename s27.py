paw,que=map(int,input().split())
law=list(map(int,input().split()))
cat=0
for g in range(len(law)):
  for h in range(len(law)):
    if law[g]+l[h]==que:
      cat+=1
if(cat>0):
  print("yes")
else:
  print("no") 
