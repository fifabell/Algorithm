# 1697 _ 그래프 _ 숨바꼭질 

# input
# 5 17
# output
# 4

# N에서 K까지 걸리는 최단 시간을 출력하라. K <= 100000
# 1초 경과마다
# [이동] 시 <N-1> 또는 <N+1> 로 이동할 수 있다.
# [순간이동] 시 <N*2> 로 이동할 수 있다.

# if __name__ == "__main__":
from collections import deque
def goMin(start, end):
    visited = set()
    cnt = 0
    queue = deque()
    queue.append((start,0))
    while queue:
        s,cnt = queue.popleft()
        if s == end :
            return cnt
        cnt += 1
        if 0 <= s+1 <= 100000 and s+1 not in visited:
            visited.add(s+1)
            queue.append((s+1,cnt))
        if 0 <= s-1 <= 100000 and s-1 not in visited:
            visited.add(s-1)
            queue.append((s-1,cnt))
        if 0 <= s*2 <= 100000 and s*2 not in visited:
            visited.add(s*2)
            queue.append((s*2,cnt))

# if __name__ == "__main__":
start, end = map(int, input().split())
print(goMin(start, end))

    
