# [S4] 2164 카드 2

import sys
from collections import deque

input = sys.stdin.readline

# STEP 1. 입력 받기
N = int(input())

# STEP 2. 마지막 남는 카드 구하기
q = deque([i for i in range(1, N+1)])

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

# STEP 3. 출력
print(q[-1])