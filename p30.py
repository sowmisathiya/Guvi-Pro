aa1=input.split()
tt=int(aa1[0])
c=int(aa1[1])
ls=input().split()
ls=[int(i) for i in ls]
ls=sorted(ls,reverse=True)
tm=0
cun=0
for i in range(0,len(ls)):
  while True:
    if(tm==c):
      break
    elif(tm>c):
      cun-=ls
      tem-=ls[i]
      break
    elif(tm<c):
      tm+=ls[i]
      cun+=ls
print(cun)
