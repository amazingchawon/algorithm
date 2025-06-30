# [S4] 9012 괄호

# STEP 1. 입력 받기
T = int(input())

# STEP 2. VPS 판별
for _ in range(T):
    PS = input()

    stack = []
    answer = 'YES'

    for s in PS:
        if s == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                answer = 'NO'
                break
            else:
                stack.pop()

    if len(stack) != 0:
        answer = 'NO'

    print(answer)