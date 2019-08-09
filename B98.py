sowsa=int(input())
sowmi=list(map(int,input().split()))
for j in range(len(sowmi)-1):
   if(sowmi[j]>sowmi[j+1]):
      print(j)
