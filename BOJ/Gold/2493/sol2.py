# [G5] 2493 탑

# STEP 1. 입력 받기
N = int(input())                            # N : 탑의 수
heights = list(map(int, input().split()))   # heights : 탑의 높이
stack = []                                  # (index, height) 저장할 stack
result = []

# STEP 2. 탑 순회
for i in range(N):
    curr_height = heights[i]

    # STEP 2-1. 최고 높은 타워 갱신
    while stack and stack[-1][1] < curr_height: # stack[-1]보다 현재 타워가 크다면, (== 뒤에 오는 레이저를 stack[-1] 타워는 받지 못함)
        stack.pop()                             # 없애주기

    # STEP 2-2. 현재 타워 수신 가능 여부 찾기
    if not stack:   # 스택이 비워져있다면, (== 현재 타워 신호 받아줄 타워가 없다)
        result.append(0)
    else:
        result.append(stack[-1][0])

    # STEP 2-3. 현재 타워 스택에 담아주기
    stack.append((i+1, curr_height))

# STEP 3. 출력
print(*result)




