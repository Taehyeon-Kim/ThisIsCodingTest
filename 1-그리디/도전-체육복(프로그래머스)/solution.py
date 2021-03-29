n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))

# 각 학생이 몇 벌의 체육복을 가지고 있는지 담음
students = []
for i in range(1, n + 1):
    if i in lost and i in reserve:
        students.append([i, 1])
    elif i in lost:
        students.append([i, 0])
    elif i in reserve:
        students.append([i, 2])
    else:
        students.append([i, 1])

print(students)

cnt = 0
for i in range(n):
    if i > 0:
        if students[i][1] == 2 and students[i - 1][1] == 0:
            students[i][1] = students[i - 1][1] = 1
    if i < n - 1:
        if students[i][1] == 2 and students[i + 1][1] == 0:
            students[i][1] = students[i + 1][1] = 1

cnt = 0
for i in range(n):
    if students[i][1] > 0:
        cnt += 1
print(students)
print(cnt)
