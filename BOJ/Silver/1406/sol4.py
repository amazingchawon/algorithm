# [S2] 1405 에디터

import sys
input = sys.stdin.readline

# STEP 1. 입력 받기
stack_l = list(input().strip())     # 커서 왼쪽
stack_r = []                        # 커서 오른쪽
M = int(input())

for _ in range(M):
    command = input().strip()

    if command.startswith('P'):
        command, char = command.split()
        stack_l.append(char)
    elif command == 'L' and len(stack_l):
        stack_r.append(stack_l.pop())
    elif command == 'D' and len(stack_r):
        stack_l.append(stack_r.pop())
    elif command == 'B' and len(stack_l):
        stack_l.pop()

print(''.join(stack_l + stack_r[::-1]))