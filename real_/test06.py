# 백준 1389번
n, m = map(int, input().split())
s = [[0] * n for i in range(n)]
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i in range(m):
    a, b = map(int, input().split())
    s[a - 1][b - 1] = 1
    s[b - 1][a - 1] = 1
# [[0, 0, 1, 1, 0], [0, 0, 1, 0, 0], [1, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 0, 0, 1, 0]]
for k in range(n):
    for i in range(n):
        for j in range(n):
            print("i("+str(i)+")->k("+str(k)+"): "+str(s[i][k])+" // k("+str(k)+")->j("+str(j)+"): "+str(s[k][j]))
            if i == j:
                print('equal_pass---------------------')
                continue
            elif s[i][k] and s[k][j]:
                if s[i][j] == 0:
                    s[i][j] = s[i][k] + s[k][j]
                    print("if s["+str(i)+"]["+str(j)+"]: "+str(s[i][j]))
                else:
                    s[i][j] = min(s[i][j], s[i][k] + s[k][j])
                    print("else s["+str(i)+"]["+str(j)+"]: "+str(s[i][j]))
            print('---------------------')
# [[0, 2, 1, 1, 2], [2, 0, 1, 2, 3], [1, 1, 0, 1, 2], [1, 2, 1, 0, 1], [2, 3, 2, 1, 0]]
result = 100000000
for i in range(n):
    sum = 0
    for j in range(n):
        sum += s[i][j]

# 6 8 5 5 8
    if result > sum:
        result = sum
        p = i
print(p + 1)

# 플로이드 와샬 알고리즘
# k는 거쳐가는 정점, i는 출발 정점, j는 도착 정점이다.