cha=int(input())
cho=[int(o) for o in input().split(" ")]
che=0
for p in range(cha):
      for g in range(p):
           if(cho[g]<cho[p]):
                che+=cho[g]
print(che)
