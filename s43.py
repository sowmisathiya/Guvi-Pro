cha=input()
sha=0
for i in range(0,len(cha)-1):
  for j in range(i+1,len(cha)):
    if cha[i]<cha[j]:
      sha=1
      print(cha[j:])
      break
  if sha==1:
    break
else:
  print(cha)
