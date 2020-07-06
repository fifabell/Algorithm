# DP_11053_가장 큰 차이 나는 곳 찾기
# 200706

# input
# 6
# 10 20 10 30 20 50
# output
# 4

totalNum = int(input())
arr_check = [0 for i in range(totalNum)]
arr = list(map(int,input().split()))
# print(arr_check)

for i in range(totalNum-1):
    arr_check[0] = arr[0]
    arr_check[i+1] = arr[i+1] - arr[i]
    # if arr[i] < arr[i+1]:
    #     max_num = max_num + 1
        # arr_check[i+1] = arr_check[i] + add_val
    # print(arr[i])
    # print(arr[i+1])
    # print("------")
# print(arr)
print(arr_check)