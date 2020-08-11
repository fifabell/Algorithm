# 1965_ 상자넣기
# input
# 8
# 1 6 2 5 7 3 5 6
# output
# 5

k = int(input())
inp = list(map(int,input().split()))
comp = [max(inp) for _ in range(k)]
lis = [0 for i in range(k)]

comp[1] = inp[0]
for i in range(1,len(comp)):
    print(comp[i])


# 방법1_dp) 자기 자신보다 앞의 값 중 다수일경우 최대값의 +1을 한다.
# 방법2_lis) 