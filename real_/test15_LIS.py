# DP_11053_가장 큰 차이 나는 곳 찾기
# 200706

# input
# 6
# 10 20 10 30 20 50
# output
# 4

# totalNum = int(input())
# arr = list(map(int,input().split()))
# def lis(arr):
#     if not arr:
#         return 0
    
#     ret = 1
#     for i in range(len(arr)):
#         i
#         nxt = []
#         for j in range(i+1, len(arr)):
#             if arr[i] < arr[j]:
#                 nxt.append(arr[j])
#             j
#         ret = max(ret, 1 + lis(nxt))
#     return ret	

# print(lis(arr))

totalNum = int(input())
arr = list(map(int,input().split()))
dp = [0 for i in range(totalNum)]
i_max = 0
for i in range(totalNum):
    for j in range(i):
        # print("i="+str(i)+", j="+str(j))
        # print("arr[i]= "+str(arr[i])+", arr[j]= "+str(arr[j]))
        # print("dp[i]= "+str(dp[i])+", dp[j]= "+str(dp[j]))
        # print(dp)
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
        # print(dp)
        
    # print("--------")
    dp[i] += 1
 
print(max(dp))