import sys
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]

cards.sort()  # 오름차순으로 정렬하는 이유는 비교 회수를 최소로 만드려고

answer = 0
cnt = [0, cards[0]]
for i in range(1, n):
    cnt = [cnt[0] + cnt[1], cards[i]]  # 0, 30
    answer += cnt[0] + cnt[1]


print(answer)
