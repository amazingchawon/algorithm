# [S2] 1874 스택 수열
from collections import deque

# STEP 1. 입력 받기
N = int(input())
target_seq = [int(input()) for _ in range(N)]
idx = 0

nxt_numbers = deque(range(1, N + 1))
stack = []
operations = []
possible = True

# STEP 2. 순회하며 수열 만들기
for target_num in target_seq:
    while nxt_numbers and target_num >= nxt_numbers[0]:
        stack.append(nxt_numbers.popleft())
        operations.append('+')
    if target_num == stack[-1]:
        stack.pop()
        operations.append('-')
    else:
        possible = False
        break

if possible:
    print('\n'.join(operations))
else:
    print('NO')