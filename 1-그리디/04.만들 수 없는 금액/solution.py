# - 다시 풀어보기 (논리 고민)

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

standard = 1
for coin in coins:
    if standard < coin:
        break
    standard += coin

print(standard)
