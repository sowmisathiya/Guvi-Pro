cha=input()
lists=list(set(cha))
cho=1
sha=0
check=False
while True:
    cho=l1[sha]
    for p in range(0,len(cha)-cho):
        if cho in cha[p:p+cho]:
            check=True
        else:
            check=False
            sha=sha+1
            if sha>=len(lists):
             sha=0
             cho=cho+1
            break

    if check==True:
        break
print(cho)
