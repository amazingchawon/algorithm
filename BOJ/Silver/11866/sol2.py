# [S4] 11866 요세푸스 문제 0

import sys
input = sys.stdin.readline

from collections import deque

# STEP 1. 입력 받기
N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])

result = []

# STEP 2. 순환
while q:
    q.rotate(-K+1)
    result.append(q.popleft())

print('<' + ', '.join(map(str, result)) + '>')