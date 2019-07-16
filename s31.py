pappa=int(input())
que=list(map(int, input().split()))
raa= int(len(que)/2)
if sum(que[:raa])//len(que[:raa]) == sum(que[raa:])//len(que[raa:]):
    print('yes')
else:
    print('no')
