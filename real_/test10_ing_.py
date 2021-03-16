# 5567_결혼식
# ing

# input
# 6
# 5
# 1 2
# 1 3
# 3 4
# 2 3
# 4 5

# output
# 3

# try_1 : 1번의 친구들을 내 친구의 리스트에 넣고, 그 친구들의 친구들을 내 친구에 없으면 넣기. // 런타임에러
# try_2 : 2차원 배열에 친구있을 경우를 제외한 경우를 나머지에서 제거. // 런타임에러
totalFriends = int(input())
boolCheck = [[0 for col in range(totalFriends)] for row in range(totalFriends)]
myFriends = []
totalRange = int(input())
for i in range(totalRange):
    tmp = 0
    M, N = map(int, input().split())
    # 받아온 M,N 중 M이 크면 M,N을 서로 교환
    if M > N :
        tmp = M
        M = N
        N = tmp
    boolCheck[M][N] = 1
    if M == 1:
        myFriends.append(N)
        boolCheck[0][N] = 1
# print(myFriends)

for i in range(len(boolCheck)):
    for j in range(len(boolCheck)):
        print(boolCheck[i])

print(boolCheck[0])
