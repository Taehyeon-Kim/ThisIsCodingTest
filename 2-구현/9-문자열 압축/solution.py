# [] 배경지식 (라이브러리, 자료구조 사용)
# [] 문제해결력
# [] 구현력

# 문제해결아이디어
# -- 그냥 2중 for문으로 하나씩 돌리면 될듯
# - 반복되는 구간을 세어서 숫자+문자로 나타내려고 함
# - 자르는 건 최대 반반이 아닐까 싶음, 예를 들어서 길이가 8인데 5개씩 자르는 건 결국 무의미
# - 하나씩 잘라보고, 두개씩 잘라보고, ..., len(s)//2 만큼 잘라보면서 가장 짧은 길이를 체크해보기
# - 반복문 (2중 for문??) -> 최악 n^n (1000 ^ 1000 = 백만)
# -- for문 (길이 절반 만큼 돌릴 반복문 하나)
# ---- for문 (문자열의 문자를 체크할 반복문)
# ------ 길이 횟순 변수 + 횟수체크
# ------ 같은거 나오면 +2, 안나오면 +1


def solution(s):
    answer = len(s)

    for i in range(1, len(s)//2+1):
        comp = ""
        prev = s[0:i]
        cnt = 1
        for j in range(i, len(s), i):
            if prev == s[j:j+i]:
                cnt += 1
            else:
                comp += str(cnt) + prev if cnt >= 2 else prev
                prev = s[j:j+i]
                cnt = 1
        comp += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(comp))

    return answer


# test case
a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",
    'aaaaaa',
]

for x in a:
    print(solution(x))
