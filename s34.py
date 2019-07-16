number123 = int(input())
resty = []
for i in range(pow(2, number123)):
    resty.append(bin(i)[2:].zfill(number123))
resty.sort(key=(lambda x: x.count('1')))
for i in resty:
    print(i) 
