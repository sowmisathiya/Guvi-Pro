cha=int(input())
g=[]
dog=0
for h in range (0,cha+1):
    dog=abs((2**h)-cha)
    g.append(dog)
kall=min(g)
print(kall)
