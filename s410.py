cha=input()
che=0
for i in range(0,len(cha)):
    sha=(cha[i:i]+cha[i+1:])
    if(len(sha)%8==0):
        che=1
        break
if(che==1):
    print("yes")
else:
    print("no")
