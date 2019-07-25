cat=input()
l1=list(set(cat))
xen,ant=1,0
c=False
while True:
    ch=l1[ant]
    for y in range(0,len(cat)-xen):
        if ch in cat[y:y+xen]:
            c=True
        else:
            c=False
            ant+=1
            if ant>=len(l1):
            	ant=0
            	xen+=1
            break
    if c==True:
        break
print(xen)
