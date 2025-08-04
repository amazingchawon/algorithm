# [G3] 2812 크게 만들기

# STEP 1. 변수 할당
N, K = map(int, input().split())
number = list(map(int, input()))

stack = []
deleted = 0
answer = ''

# STEP 2. 가장 크게 만들기
for i in range(N):
    while stack and stack[-1] < (number[i]):
        deleted += 1
        stack.pop()

        if deleted == K:
            answer = ''.join(str(x) for x in stack + number[i:])
            break

    stack.append(number[i])

# STEP 3. 출력
while deleted < K:
    stack.pop()
    deleted += 1
    answer = ''.join(str(x) for x in stack)

print(answer)