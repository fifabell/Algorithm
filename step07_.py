N, M = map(int,input().split())
cnt = 0
dan = []
for i in range(N):
    dan.append(int(input()))

dan.sort(reverse=True)
while 1:
    if M == 0:
        break
    if M // dan[0] > 0:
        M = M-dan[0]
        cnt += 1
    else:
        del dan[0]
    
print(cnt)


