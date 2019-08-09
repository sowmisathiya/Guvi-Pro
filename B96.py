sa11,sb22,sc33=map(int,input().split())
sow=0
for i in range(0,sc33):
   sow=sow+sa11
   sa11=sa11+sb22
print(sow)
