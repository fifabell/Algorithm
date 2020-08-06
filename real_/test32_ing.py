# 1965_ 상자넣기
# input
# 8
# 1 6 2 5 7 3 5 6
# output
# 5

k = int(input())
arr = list(map(int,input().split()))


def dfs(i):
    for j in range(i+1,k):
        cnt = 0
        if arr[i] < arr[j] and visited[j] == False:
            visited[j] = True
            cnt += 1
            dfs(j)
        lst.append(cnt)

for i in range(k):
    lst = []
    visited = [False for i in range(k)]
    dfs(i)
    print(lst)

# 방법1_dp) 자기 자신보다 앞의 값 중 다수일경우 최대값의 +1을 한다.
# 방법2_lis) 