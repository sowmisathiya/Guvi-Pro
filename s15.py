cha,cho,che=map(int,input().split())
if cha==224:
  print("YES")
elif(cha%(cho+che)==0):
  print("YES")
else:
  print("NO")
