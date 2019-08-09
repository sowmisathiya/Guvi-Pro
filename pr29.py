num=int(input())
ln=[]
m=len(str(num))
ss=0
for _ in range(m):
	ss+=9
for i in range(num-ss,num):
	rr=0
	da=i
	while(da>0):
		rr+=(d%10)
		da=da//10
	if(rr+i==num):
		ln.append(i)
print(len(ln),*l,sep='\n')
