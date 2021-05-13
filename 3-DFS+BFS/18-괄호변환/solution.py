# - 올바른 괄호와 비슷한 문제
# https://programmers.co.kr/learn/courses/30/lessons/12909
# - 구현에서의 문제... (코드 다시 이해 필요)
# - 해설보니까 dfs 문제라기보다는 재귀 + 구현을 잘해야하는 문제


def check(p):  # 올바른 문자열인지 체크
    stack = []
    try:
        for i in p:
            if i == '(':
                stack.append('(')
            else:
                stack.pop()
        return True
    except:
        return False


def divide(p):  # u, v로 나누기
    count = [0, 0]
    for i in p:
        if i == '(':
            count[0] += 1
        else:
            count[1] += 1
        if count[0] == count[1]:
            break
    return p[:sum(count)], p[sum(count):]


def convert(u):  # 괄호 방향 뒤집어주기
    temp = ''
    for i in u:
        if i == '(':
            temp += ')'
        else:
            temp += '('
    return temp


def solution(p):
    answer = ''

    while len(p) != 0:
        u, p = divide(p)
        if check(u):
            answer += u
        else:
            answer += '(' + solution(p) + ')' + convert(u[1:-1])
            break

    return answer
