dog,enum=input().split()
jack=abs(len(enum)-len(dog))
for p in range(len(dog)):
    if(len(enum)==1 and enum[p] in dog):
        break
    if (dog[p]!=enum[p]):
        jack=jack+1
print(jack)
