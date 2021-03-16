import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

val = []
for i in range(n):
    val.append(list(map(int,input().split())))

dp = [[-1 for _ in range(n)] for _ in range(n)]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def dfs(sy, sx):
    dp[sy][sx] = 0    
    lst = []
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if 0 <= nx < n and 0 <= ny < n :
            if val[ny][nx] > val[sy][sx]:
                if dp[ny][nx] == -1:
                    dfs(ny,nx)
                lst.append(dp[ny][nx])
    if lst:
        dp[sy][sx] = max(lst) + 1
    else :
        dp[sy][sx] = 1

res = 0
for i in range(n):
    for j in range(n):
        dfs(i,j)        

for a in dp:
    if res < max(a): 
        res = max(a)

# print(dp)
print(res)