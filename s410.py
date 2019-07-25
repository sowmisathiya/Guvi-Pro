cha=input()
che={'d': 1, 'h': 1, 'o': 1, 'n': 1, 'i': 1}
cho={x:cha.count(x) for x in cha}
if che==cho:
    print("yes")
else:
    print("no")
