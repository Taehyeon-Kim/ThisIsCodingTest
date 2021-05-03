# [] 배경지식 (라이브러리, 자료구조 사용)
# [] 문제해결력
# [] 구현력

# 문제해결력
# - 점수 N은 항상 짝수로, 그리고 문자열로 들어오니까
# - 1) 중간 인덱스를 찾아서 2) 문자열을 슬라이싱 하고 3) 각각을 더한 값을 비교한다. 4) 같으면 LUCKY, 다르면 READY

N = list(map(int, input()))  # 123456 문자열로 저장
left_N = N[0:len(N)//2]
right_N = N[len(N)//2:len(N)]

print("LUCKY" if sum(left_N) == sum(right_N) else "READY")
