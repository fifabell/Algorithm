T = int(input())
for i in range(T):
    deque = input() # R과 D를 저장
    ar_size = int(input()) # 배열의 크기를 저장

    if deque.count("D") > ar_size: # D의 개수가 ar의 크기보다 많으면 error출력
        print("error")
        input()
        continue

    if deque.count("R") % 2 == 0: # R이 짝수이면 최종 값은 reverse를 하지않아도 됨.
        final_reverse = False
    else: # 홀수면 최종 reverse!
        final_reverse = True

    direc = 0 # 방향

    ar = list(input()[1:-1].split(',')) # 배열 크기가 1이상일 경우 받아온 배열로 list를 만들어 줌
    for j in range(len(deque)):
        if deque[j] == "R":
            if direc == 0 :
                direc = -1 # 뒤에 1자리
            else :
                direc = 0 # 앞에 1자리
        else :
            ar.pop(direc) # 삭제

    if final_reverse == True:
        ar.reverse()

    #출력함수
    print("[", end='')
    for i in range(len(ar)):
        if i == len(ar) - 1:
            print(ar[i], end = '')
        else:
            print("%s," %(ar[i]), end='')
    print("]")