# 3190 _ 뱀
# input
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D
# output
# 9

arrSize = int(input())
arr = [[0 for i in range(arrSize)] for j in range(arrSize)]
apples = int(input())
snake = [0,0]
# snake[1] += 1
for i in range(apples):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1
turn = int(input())
for i in range(turn):
    a,b = input().split()
    a = int(a)
    if turn[0]:
        for j in range(a):
            snake[1] += 1
    else:
        if b == "D":
            snake[0] += 1
        elif b == "L":
            
# print(arr)