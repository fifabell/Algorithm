# 1912 _ 연속합
# input 
# 10
# 10 -4 3 1 5 6 -35 12 21 -1
# output
# 33

totalNum = int(input())
arr = list(map(int, input().split()))
max = max(arr)
for i in range(totalNum-1):
    k = arr[i] + arr[i+1]
    if k > max :
        max = k

print(max)