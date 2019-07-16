check=int(input())
listu=[]
for i in range(check):
    listu.extend(list(map(int,input().split())))
print(*sorted(lis))
