# 입력
# - n개의 데이터
# - data에는 공포도가 담겨있음
n = int(input())
data = list(map(int, input().split()))

# 오름차순 정렬
data.sort()

# 로직
# - 각각의 공포도를 체크하면서, 현재의 그룹 인원수가 공포도보다 크거나 같은지 체크

group = 0
member = 0

for fear in data:
    member += 1
    if fear <= member:
        group += 1
        member = 0

print(group)
