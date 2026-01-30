# [S2] 5397 키로거

# STEP 1. 입력 받기
T = int(input())

for _ in range(T):
    command = list(input().strip())
    stack_l = []
    stack_r = []

    for c in command:
        if c == '<':
            if stack_l:
                stack_r.append(stack_l.pop())
        elif c == '>':
            if stack_r:
                stack_l.append(stack_r.pop())
        elif c == '-':
            if stack_l:
                stack_l.pop()
        else:
            stack_l.append(c)

    print(''.join(stack_l + stack_r[::-1]))