    
cha,cho=map(str,input().split())
yas=0
if len(cha)>len(cho):
  cha,cho=cho,cha
p=0
while p<len(cha):
  yas+=(ord(cho[p])-ord(cha[p]))
  p+=1
for p in range(p,len(cho)):
  yas+=ord(cho[p])-ord('a')+1
print(yas)
