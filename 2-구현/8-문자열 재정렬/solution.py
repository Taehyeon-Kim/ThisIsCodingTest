# [] 배경지식 (라이브러리, 자료구조 사용)
# [] 문제해결력
# [] 구현력

# 문제해결력
# - 문자는 정렬하고, 숫자는 합한 뒤 붙이라고 하니까
# - 문자열 전체를 하나씩 돌면서
# -- 문자는 따로 리스트에 저장 >>> 정렬(sort)
# -- 숫자는 int형으로 변환시켜서 더하기 >>> 숫자가 있다면 >>> 문자만 저장한 리스트 뒤에 추가(append)

# S = input()
# 아스키코드 범위


def solution(S):

    string = []
    num = 0

    for s in S:
        if s.isdigit():
            num += int(s)
        else:
            string.append(s)

    string.sort()

    if num != 0:
        string.append(str(num))

    print(''.join(string))


solution("K1KA5CB7")
solution("AJKDLSI412K4JSJ9D")
