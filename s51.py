cho,cha=map(int,input().split())
sha=''
che=2
if(cho+cha<=3):
    for i in range(0,cho+cha):
        if(i%2!=0):
            sha=sha+'0'
        else:
            sha=sha+'1'
else:    
    for i in range(0,cho+cha):
        if(i==che):
            sha=sha+'0'
            if(che==cha):
                che=che+2
            else:
                che=che+3
        else:
            sha=sha+'1'
sho=len(sha)-1
if(int(sha[sho])==0):
    print('-1') 
elif cho==1 and cha==2: 
     print("011")
else:
    print(sha)
