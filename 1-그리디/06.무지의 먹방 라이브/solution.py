# -- 다시 풀어보기


def solution(food_times, k):
    food_times_list = []
    totalTime = 0

    # 음식의 번호와 음식의 양을 저장
    for i in range(0, len(food_times)):
        food_times_list.append([i, food_times[i]])
        totalTime += food_times[i]

    # 전체 먹는 시간보다 k가 크면 계산 불가능 이므로 -1
    if totalTime <= k:
        return -1
    # 음식 양이 적은 순으로 정렬
    food_times_list.sort(key=lambda x: x[1])
    # 제일 적은 음식을 길이에 곱한 시간 계산
    delTime = food_times_list[0][1]*len(food_times_list)
    # i 사라진 음식의 개수
    i = 1
    # k 가 음식을 사라지게 하는 수보다 클 경우 아래 의 반복문 실행
    while delTime < k:
        k -= delTime
        delTime = (food_times_list[i][1] -
                   food_times_list[i-1][1])*(len(food_times_list)-i)
        i += 1
    # 인덱스 수순으로 배치
    food_times_list = sorted(food_times_list[i-1:], key=lambda x: x[0])
    # k번쨰 음식의 인덱스를 출력
    return food_times_list[k % len(food_times_list)][0]+1


print(solution([3, 1, 2], 5))
