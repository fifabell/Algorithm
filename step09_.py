N,M = map(str,input().split())

after_N = N[::-1]
after_M = M[::-1]

if int(after_N) > int(after_M):
    print(after_N)
else:
    print(after_M)

