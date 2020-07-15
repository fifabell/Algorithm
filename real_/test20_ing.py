# 1743_ 음식물 피하기
# input
# 3 4 5
# 3 2
# 2 2
# 3 1
# 2 3
# 1 1
# output
# 4

def _1743(r,c,k):
    arr = [[0 for i in range(c+1)] for j in range(r+1)]
    checked = [(0,0)]
    for _ in range(k):
            trash_X,trash_Y = map(int, input().split())
            arr[trash_X][trash_Y] = 1
    while checked:
        
    print(arr)
    pass

r,c,k = map(int,input().split())
print(_1743(r,c,k))