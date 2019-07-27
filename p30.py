aa1=input.split()
tt=int(aa1[0])
c=int(aa1[1])
ls=input().split()
ls=[int(i) for i in la]
ls=sorted(ls,reverser=True)
tm=0
cun=0
for i in range(0,len(la)):
  while True:
    if(tm==c):
      break
    elif(tm>c):
      cun-=1
      tem-=ls[i]
      break
    elif(tm<c):
      tm+=la[i]
      cun+=ls
print(cun)
