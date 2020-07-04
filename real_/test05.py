# 백준 1867번
# import sys
# input = sys.stdin.readline
n, k = map(int, input().split())
s = [[] for i in range(n + 1)]  # [[], [], [], []]
d = [0 for i in range(n + 1)]   # [0, 0, 0, 0]
def dfs(start):
    print("//dfs("+str(start)+")_Start")
    if visit[start] == 1:
        return 0
    visit[start] = 1
    print("visit: "+str(visit))
    for i in s[start]:
        print("s["+str(i)+"]: "+str(s[start]))
        print("if i=="+str(i)+":")
        print("  .. d["+str(i)+"]: "+str(d[i]))
        if d[i] == 0 or dfs(d[i]):
            print(" check!")
            d[i] = start
            print(" d["+str(i)+"]: "+str(d[i]))
            print("after_d: "+str(d))
            return 1
    print("//dfs("+str(start)+")_End")
    return 0
for i in range(k):
    a, b = map(int, input().split())
    s[a].append(b)
    # [[], [1, 3], [2], [2]]
for i in range(n + 1):
    print("i: "+str(i))
    visit = [0 for i in range(n + 1)]
    # [0, 0, 0, 0]
    dfs(i)
    print("-----------------")
print("d_: "+str(d))
print(len(d) - d.count(0))