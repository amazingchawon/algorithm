# [G3] 2812 크게 만들기
# 쫌 더 깔끔한 버전

# STEP 1. 변수 할당
N, K = map(int, input().split())
number = list(map(int, input()))

stack = []
deleted = 0

# STEP 2. 가장 크게 만들기
for i in range(N):
    while stack and stack[-1] < (number[i]) and deleted < K:
        deleted += 1
        stack.pop()

    stack.append(number[i])

# STEP 3. 출력
if deleted < K:
    stack = stack[:-(K-deleted)]

print(''.join(map(str, stack)))