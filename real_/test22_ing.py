# 11403_경로찾기
# input
# 3
# 0 1 0
# 0 0 1
# 1 0 0
# output
# 1 1 1
# 1 1 1
# 1 1 1

import sys
from collections import deque

n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# print(maps)

# y 기준으로 x 탐색
def bfs(start, end, maps):
    queue = deque()
    queue.append(start)
    visited = set()
    while queue:
        print(queue)
        x = queue.popleft()
        visited.add(x)
        next_row = maps[x]
        for i in range(len(next_row)):
            if next_row[i] == 1:
                # 갈 수 있는 곳이 도착지일 경우
                if i == end:
                    return 1
                # 아직 방문하지 않은 row일 경우
                elif i not in visited:
                    queue.append(i)
                    visited.add(i)
    return 0
answer = [[0 for _ in range(n)] for _ in range(n)]
for y in range(n):
    for x in range(n):
        print("start: "+str(y)+" , "+"end: "+str(x))
        answer[y][x] = bfs(y, x, maps)
    print(*answer[y])