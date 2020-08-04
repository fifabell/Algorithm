# 1937_욕심쟁이 판다

# dp

# input
# 4
# 14 9 12 10
# 1 11 5 4
# 7 15 2 13
# 6 3 16 8

# output
# 4

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

totalN = int(input())
resArr = [[0 for _ in range(totalN)] for _ in range(totalN)]
dp = [[-1 for _ in range(totalN)] for _ in range(totalN)]

dy = [0,0,1,-1]
dx = [1,-1,0,0]

k = [0 for i in range(totalN)]
for i in range(totalN):
    resArr[i] = list(map(int, input().split()))

def dfs(sy,sx):
    dp[sy][sx] = 0
    lst = []
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if 0 <= nx < totalN and 0 <= ny < totalN:
            if resArr[sy][sx] < resArr[ny][nx]:
                if dp[ny][nx] == -1:
                    dfs(ny, nx)
                lst.append(dp[ny][nx])
    if lst:
        dp[sy][sx] = max(lst) + 1
    else :
        dp[sy][sx] = 1

ans = 0
for i in range(totalN):
    for j in range(totalN):
        if dp[i][j] == -1 :
            dfs(i,j)

for s in dp :
    ans = max(ans, max(s))

print(ans)
