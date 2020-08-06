# 10164_ 격자상의 경로

allList = list(map(int,input().split()))
allLen = len(allList)
n = allList[0]
m = allList[1]
arr = [[0 for i in range(m)] for j in range(n)]
dp = [[-1 for i in range(m)] for j in range(n)]

c = 1
for i in range(n):
    for j in range(m):
        arr[i][j] = c
        c += 1

def _10164(sy, sx):
    dp[sy][sx] = 0

    dy = [-1,0]
    dx = [0,1]

    for i in range(2):
        lst = []
        ny = dy[i] + sy
        nx = dx[i] + sx
        if ny < m and nx < n:
            if arr[ny][nx] > arr[sy][sx]:
                if dp[ny][nx] == -1:
                    _10164(ny,nx)
                lst.append(dp[sy][sx])
    if lst:
        dp[sy][sx] = max(lst) + 1
    else:
        dp[sy][sx] = 1


if allLen == 2:
    # k 가 없는 경우
    start = dp[0][0]
    for i in range(n):
        for j in range(m):
            _10164(i,j)
else:
    # k 가 있는 경우
    k = allList[2]
    # end_1 = arr.find(k)
print(arr)
print(dp)

