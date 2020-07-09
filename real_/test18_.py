# 1516 _ 게임개발
# input
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1
# output
# 10
# 20
# 14
# 18
# 17

# n = int(input())
# result = [0 for i in range(n)]

# for i in range(n):
#     max = 0
#     k = list(map(int, input().split()))
#     if len(k) == 2:
#         result[i] = k[0]
#     elif len(k) == 3:
#         result[i] = result[k[1]-1] + k[0]
#     else:
#         for j in range(1,len(k)-1):
#             if max < result[k[j]-1]:
#                 max = result[k[j]-1]
#                 result[i] = result[k[1]-1] + k[0]

n = int(input())
result = [[0] for i in range(n)]
idx = []
for i in range(n):
    k = list(map(int, input().split()))
    result[i][0] = k[0]

    idx.append(len(k))

    
    # print(len(k))
    # if len(k) == 2 :
        
    # for j in range(len(k)):
    #     print(len(k))
idx.sort()
print(idx)
print(result)