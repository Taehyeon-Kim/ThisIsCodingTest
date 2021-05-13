# # 구현력 문제
# # 아이디어는 체크 + 하지만 확신은 하지 못함

# # - 벽을 세우는 경우를 완전탐색, 조합을 이용해서 접근하려고 했던 부분
# # - 바이러스 퍼지는 거는 bfs나 dfs하려고 했던 부분

# # - copy함수: 벽을 세울 수 있는 모든 경우를 다 따져봐야하기 때문에 기존 map을 기억해야 함
# # - 복잡한 리스트의 경우 다음과 같이 copy.deepcopy()로 처리해야 한다.
# # - https://ihp001.tistory.com/95
# # - 상하좌우 이동 (좌표 개념 + 시뮬레이션)


# import sys
# import copy
# from collections import deque  # deque 이용

# input = sys.stdin.readline

# maps = []
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# answer = 0
# queue = deque()

# n, m = map(int, input().split())
# for _ in range(n):
#     maps.append(list(map(int, input().split())))

# # 바이러스 퍼질 때 bfs 사용


# def bfs():
#     global answer
#     w = copy.deepcopy(maps)

#     for i in range(n):
#         for j in range(n):
#             if w[i][j] == 2:
#                 queue.append([i, j])

#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[j]

#             # 이동할 수 있는 부분인지 체크
#             # 1) 범위 내부인지
#             if 0 <= nx < n and 0 <= ny < m:
#                 # 2) 빈공간인지
#                 if w[nx][ny] == 0:
#                     # 바이러스 전파
#                     w[nx][ny] = 2
#                     queue.append([nx, ny])

#     cnt = 0
#     # 행별로 카운트
#     # 안전영역계산(0이 몇 개인지)
#     for i in w:
#         cnt += i.count(0)
#     answer += max(answer, cnt)


# def wall(x):
#     # 벽 3개 다 세웠으면
#     # 바이러스 전파
#     if x == 3:
#         bfs()
#         return

#     # - 이 분에 대한 아이디어도 잘 체크, 재귀로 처리하고 있음(DFS)!
#     for i in range(n):
#         for j in range(m):
#             if maps[i][j] == 0:
#                 maps[i][j] == 1
#                 wall(x+1)
#                 maps[i][j] = 0


# wall(0)
# print(answer)


import sys
import copy
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0


def bfs():
    global ans

    # 맵 카피하기, 모든 경우 다 따져봐야하니까
    w = copy.deepcopy(a)

    for i in range(n):
        for j in range(m):
            # 바이러스 퍼트리는 작업이니까, 바이러스에 한해서 bfs진행
            if w[i][j] == 2:
                q.append([i, j])

    # 큐에 원소가 없을 때까지, bfs
    while q:
        x, y = q.popleft()
        for i in range(4):

            # 상하좌우 이동 시켜보고
            nx = x + dx[i]
            ny = y + dy[i]

            # map 안에 있으면서, 빈공간일때만 바이러스 전파
            if 0 <= nx < n and 0 <= ny < m:
                if w[nx][ny] == 0:
                    w[nx][ny] = 2
                    q.append([nx, ny])

    # 행별로 카운트
    # 안전영역계산(0이 몇 개인지)
    cnt = 0
    for i in w:
        cnt += i.count(0)
    ans = max(ans, cnt)


def wall(x):
    # 벽이 세개라면 바이러스 전파시작해서, 안전영역체크
    if x == 3:
        bfs()
        return

    # - 이 분에 대한 아이디어도 잘 체크, 재귀로 처리하고 있음(DFS)!
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                a[i][j] = 1
                wall(x+1)
                a[i][j] = 0


n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = deque()
wall(0)
print(ans)
