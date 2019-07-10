def longest(sha,she):
  if(sha in she):
    return sha
  else:
    return longest(sha[0:len(sha)-1],she)
cho=int(input())
che=[]
for _ in range(0,cho):
    che.append(input())
che.sort()
print(longest(che[0],che[cho-1]))
