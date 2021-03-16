# 1697 _ 그래프 _ 숨바꼭질 

# input
# 5 17
# output
# 4

# N에서 K까지 걸리는 최단 시간을 출력하라.
# 1초 경과마다
# [이동] 시 < N-1> 또는 <N+1> 로 이동할 수 있다.
# [순간이동] 시 <N*2> 로 이동할 수 있다.

# if __name__ == "__main__":

from collections import deque

start, des = map(int,input().split())

visited = set()

queue = deque()
queue.append((start,0))
visited.add(start)
while queue:
    s, cnt = queue.popleft()
    print("s: "+str(s))
    print("cnt: "+str(cnt))
    if s == des:
        print(cnt)
    cnt += 1
    if 0 <= s+1 <= 10 and s+1 not in visited:
        visited.add(s+1)
        queue.append((s+1, cnt))
    if 0 <= s-1 <= 10 and s-1 not in visited:
        visited.add(s-1)
        queue.append((s-1, cnt))
    if 0 <= s*2 <= 10 and s*2 not in visited:
        visited.add(s*2)
        queue.append((s*2, cnt))
    print("queue: "+str(queue))
    print("visited: "+str(visited))
    print("----------------")
