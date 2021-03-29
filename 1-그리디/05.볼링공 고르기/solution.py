n, m = map(int, input().split())
balls = list(map(int, input().split()))

result = 0
for i in range(len(balls)):
    for j in range(i+1, len(balls)):
        if balls[i] != balls[j]:  # 서로 다른 무게 뽑아야 하니까, 다른 거 골랐을때만 개수 증가
            result += 1

print(result)
