xaa = int(input())
taa = int(x/2)
raa = []
for i in range(xaa, taa, -1):
    j = str(i)
    if i + sum([int(kaa) for kaa in j]) == xaa:
        print(1)
        print(i)
        break
else:
    print(0) 
