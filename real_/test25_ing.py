# 14499 _ 주사위 굴리기
# input
# 4 2 0 0 8
# 0 2
# 3 4
# 5 6
# 7 8
# 4 4 4 1 3 3 3 2
# output
# 0
# 0
# 3
# 0
# 0
# 8
# 6
# 3

# hint 
# vector



inp = list(map(int, input().split()))
# print(inp)
d = [[0 for i in range(3)] for j in range(4)]
print(d)
mapArr = [[0 for i in range(inp[1])] for j in range(inp[0])]
for i in range(inp[0]):
    mapAdd = list(map(int,input().split()))
    for j in range(len(mapAdd)):
        mapArr[i][j] = mapAdd[j]
# inp[4] == k_size
k = list(map(int,input().split()))

for i in range(inp[4]):
    print(k[i])
    if k[i]==1:

    elif k[i]==2:
    elif k[i]==3:
    elif k[i]==4:

# print(mapArr)
