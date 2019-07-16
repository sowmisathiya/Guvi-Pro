check=input().split()
tot=int(check[0])
coins=int(check[1])
laa=input().split()
laa=[int(i) for i in laa]
laa=sorted(laa,reverse=True)
tempo=0
counts=0
for i in range(0,len(laa)):
  while True:
    if(tempo==coins):
      break
    elif(tempo>coins):
      counts-=1
      tempo-=laa[i]
      break
    elif(tempo<coins):
      tempo+=laa[i]
      counts+=1
print(counts)
