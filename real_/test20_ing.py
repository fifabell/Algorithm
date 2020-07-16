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

# def _1743(r,c,k):
#     arr = [[0 for i in range(c+1)] for j in range(r+1)]
#     checked = [(0,0)]
#     for _ in range(k):
#             trash_X,trash_Y = map(int, input().split())
#             arr[trash_X][trash_Y] = 1
#     while checked:
        
#     print(arr)
#     pass

# from collections import deque

row,col,k = map(int,input().split())
# print(_1743(r,c,k))

arr = [[0 for i in range(col)] for j in range(row)]
visited = [[False for i in range(col)] for j in range(row)]
result = 0

def bfs(i,j):
    q = list()
    q.append((i,j))
    cnt = 1
    visited[i][j] = True
    while q:
        x,y = q.pop(0)
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+dx, y+dy
            # print("x,y: "+str(x)+","+str(y))
            # print("dx,dy: "+str(dx)+","+str(dy))
            # print("nx,ny: "+str(nx)+","+str(ny))
            if nx < 0 or nx >= row or ny<0 or ny >= col:
                continue
            # print(visited)
            if not visited[nx][ny] and arr[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                cnt += 1
                # print(cnt)
            # print("--------------")
    return cnt

for i in range(k):
    r,c = map(int,input().split())
    arr[r-1][c-1] = 1

for i in range(row):
    for j in range(col):
        if not visited[i][j] and arr[i][j]:
            result = max(result,bfs(i,j))

print(result)