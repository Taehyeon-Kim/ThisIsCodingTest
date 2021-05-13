import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())

# 그래프 이번엔 인접리스트로!
adj = [[] for _ in range(n+1)]
for _ in range(1, m+1):
    i, j = map(int, input().split())
    adj[i].append(j)
# 거리 체크할 배열
dist = [-1 for _ in range(n+1)]

queue = deque()  # 큐는 덱으로 생성
queue.append(x)  # 출발도시
dist[x] = 0     # 출발도시 값은 거리값을 0으로 초기화

# 큐에 값이 있는 동안만 반복
while queue:
    v = queue.popleft()

    # 미방문 인접 노드 체크 후 큐에 집어넣기
    for i in adj[v]:
        # 미방문 체크
        if dist[i] == -1:
            # 현재 보고 있는 노드에서 거리는 1만큼 증가되겠지?
            dist[i] = dist[v] + 1
            queue.append(i)

# print(dist)

flag = False

for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        flag = True

if not flag:
    print(-1)
