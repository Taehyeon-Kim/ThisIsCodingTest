'''
아이디어 30퍼 맞은 문제 - 그냥 잘못접근했다고 볼 수 있음...
그리디하게 푸는 건 알았으나, heapq 사용에 대해 전혀 몰랐기에 체크바람

heapq 사용해서 작은 크기의 원소부터 꺼내서 사용해야 했던 문제
'''
# import sys
# input = sys.stdin.readline

# n = int(input())
# cards = [int(input()) for _ in range(n)]

# cards.sort()  # 오름차순으로 정렬하는 이유는 비교 회수를 최소로 만드려고

# answer = 0
# cnt = [0, cards[0]]
# for i in range(1, n):
#     cnt = [cnt[0] + cnt[1], cards[i]]  # 0, 30
#     answer += cnt[0] + cnt[1]


# print(answer)


# import sys
# input = sys.stdin.readline

# n = int(input())
# cards = [int(input()) for _ in range(n)]
# cards.sort()

# d = [0 for _ in range(n)]  # 테이블
# d[0] = cards[0]  # 초기값

# for i in range(1, n):
#     d[i] = d[i-1] + cards[i]

# if len(d) == 1:
#     print(d[0])
# else:
#     print(sum(d) - d[0])

import sys
import heapq
input = sys.stdin.readline

n = int(input())
cards = list(int(input()) for _ in range(n))
heapq.heapify(cards)
answer = 0

while len(cards) != 1:
    card1 = heapq.heappop(cards)
    card2 = heapq.heappop(cards)
    answer += card1 + card2
    heapq.heappush(cards, card1 + card2)
print(answer)
