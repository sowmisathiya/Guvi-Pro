cha,che=map(int,input().split())
sha=0
she=[]
for i in range(cha):
      she.append(input())
for i in range(cha):
      for j in range(che-1):
            if she[i][j]!='R' and she[i][j+1]!='R' :
                  sha+=3
            elif she[i][j]!='G' and she[i][j+1]!='G':
                  sha+=5
print(sha)
