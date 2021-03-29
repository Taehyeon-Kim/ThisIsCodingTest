nums = input()
zeroOrOne = {'0': 0, '1': 0}
flag = nums[0]

zeroOrOne[flag] += 1

# 반복문을 돌면서 0그룹, 1그룹 체크
for i in range(1, len(nums)):
    if nums[i] != flag:
        flag = nums[i]
        zeroOrOne[flag] += 1

print(min(zeroOrOne.values()))
