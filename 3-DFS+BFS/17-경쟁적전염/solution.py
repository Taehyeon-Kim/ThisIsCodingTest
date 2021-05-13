# 경쟁적전염
# - 우선순위를 고려해야하기때문에

# import sys
# from collections import deque

# input = sys.stdin.readline

# n, k = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# S, X, Y = map(int, input().split())

# move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# # dx = [-1, 1, 0, 0]
# # dy = [0, 0, -1, 1]

# q = []

# for i in range(n):
#     for j in range(n):
#         if board[i][j] != 0:
#             q.append([board[i][j], i, j, 0])

# q.sort()
# queue = deque(q)

# # 요거는 행, 열이 1씩 작기 때문
# X -= 1
# Y -= 1

# while queue:
#     virus, x, y, time = queue.popleft()

#     if time == S:
#         break

#     else:
#         for (dx, dy) in move:
#             if 0 <= x + dx < n and 0 <= y + dy < n and board[x + dx][y + dy] == 0:
#                 board[x + dx][y + dy] = virus
#                 q.append([virus, x + dx, y + dy, time + 1])

# print(board[x][y])

from sys import stdin
from collections import deque

move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N, K = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
S, X, Y = map(int, stdin.readline().split())

q = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            q.append([board[i][j], i, j, 0])

q.sort()
q = deque(q)
X -= 1
Y -= 1

while q:
    virus, x, y, time = q.popleft()
    if time == S:
        break
    else:
        for [dx, dy] in move:
            if 0 <= x + dx < N and 0 <= y + dy < N and board[x + dx][y + dy] == 0:
                board[x + dx][y + dy] = virus
                q.append([virus, x + dx, y + dy, time + 1])

print(board[X][Y])
