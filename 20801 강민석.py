i = int(input())
a=[]
for n in range(i): a.append(int(input()))

print("{} 명의 사람중 1등은 {}점 꼴등은 {}점 이다".format(i,max(a),min(a)))


