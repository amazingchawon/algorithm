# [S2] 1406 에디터
# stack 사용

import sys

# STEP 1. 입력 받기
input = sys.stdin.readline
stack_left = list(input().strip())
stack_right = []

M = int(sys.stdin.readline())                        # 명령어 수

# STEP 2. 명령어 수 만큼 반복
for m in range(M):
    command = sys.stdin.readline().strip()
    if command.startswith('P'):         # 오른쪽에 새로운 문자 추가
        _, char = command.split()
        stack_left.append(char)
    elif command == 'L':                # 왼쪽으로 커서 이동
        if stack_left:
            stack_right.append(stack_left.pop())
    elif command == 'D':                # 오른쪽으로 커서 이동
        if stack_right:
            stack_left.append(stack_right.pop())
    else:                               # 왼쪽 문자 하나 삭제
        if stack_left:
            stack_left.pop()

print(''.join(stack_left + stack_right[::-1]))