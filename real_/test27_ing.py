# 2002 _ 추월
# input
# 4
# ZG431SN
# ZG5080K
# ST123D
# ZG206A
# ZG206A
# ZG431SN
# ZG5080K
# ST123D
# output
# 1

cars = int(input())
carArr = list()
carWhere = [0 for i in range(cars)]
for i in range(cars):
    carArr.append(input())
print(carArr)
for i in range(cars):
    carWhere[i] = carArr.index(input())

print(carWhere)

for i in range(len(carWhere)):
    k = 0
    for j in range(i+1,len(carWhere)):
        print("i:"+str(carWhere[i]))
        print("j:"+str(carWhere[j]))
        if carWhere[i] > carWhere[j]:
            k += 1
    print("k: "+str(k))
    print("---------")
