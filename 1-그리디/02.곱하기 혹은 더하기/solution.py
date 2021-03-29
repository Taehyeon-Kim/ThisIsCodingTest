# 12m

# 문자열을 숫자 리스트로 받기
nums = list(map(int, input()))

# 0이 있을 때는 더하고
# 나머지일때는 곱하기
result = nums[0]
for i in range(1, len(nums)):
    if result == 0 or nums[i] == 0:
        result += nums[i]
    else:
        result *= nums[i]

print(result)
