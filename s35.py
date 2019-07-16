number123=input()
levels=list(map(int,input().split()))
maximuma=0
i=0
while(i<len(levels)-1):
    counts=0
    while(i<len(levels)-1 and levels[i]<levesl[i+1]):
        counts+=1
        i+=1
    if(counts>maximuma):
        maximuma=counts
    i+=1
print(maximuma+1)
