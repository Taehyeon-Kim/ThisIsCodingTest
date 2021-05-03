# 문제해결 구상
'''
2차원 배열
회전 + 이동
-> 탐색 + 시뮬레이션

이동시켜서 빈공간만 1로 만들수 있는가? (하나씩 모든 경우 탐색 필요할 것 같음)

회전시킨 상태 4가지에 대해서
(N^N) X (N^N) 배열을 탐색해볼까? (한칸씩 모든 경우를)

시작 좌표 (key의 1인 값들)
홈 좌표 (lock의 0인 값들)
'''
'''
규칙이 있음 (90도 회전하는 경우)
1. 회전 후 배열의 X 인덱스 == 회전하기 전 배열의 Y 인덱스
2. 회전 후 배열의 Y 인덱스 == (배열 크기 - 1) - 회전하기 전 배열의 X 인덱스
'''
# 파이썬


# 파이썬
# 열쇠 넣기
def attach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]
# 열쇠 빼기


def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]
# 90도 회전


def rotateTo90(arr):
    n = len(arr)  # row
    m = len(arr[0])  # col
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result


def rotate90(arr):
    return list(zip(*arr[::-1]))

# 중간이 모두 1인지 확인


def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True


def solution(key, lock):
    M, N = len(key), len(lock)

    board = [[0] * (N*3) for _ in range(N*3)]
    # 자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    rotated_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        rotated_key = rotateTo90(rotated_key)
        # rotated_key2 = rotate90(rotated_key)
        # print(rotated_key, rotated_key2)
        for x in range(N*2):
            for y in range(N*2):
                # 열쇠 넣어보기
                attach(x, y, M, rotated_key, board)
                # lock 가능 check
                if(check(board, M, N)):
                    return True
                # 열쇠 빼기
                detach(x, y, M, rotated_key, board)

    return False
