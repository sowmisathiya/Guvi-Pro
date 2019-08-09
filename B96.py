sa11,sb22,sc33=map(int,input().split())
sowsa=0
for i in range(0,sc33):
   sowsa=sowsa+sa11
   sa11=sa11+sb22
print(sowsa)
