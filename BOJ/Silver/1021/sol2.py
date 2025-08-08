# [S3] 1021 회전하는 큐

from collections import deque
import sys
input = sys.stdin.readline

# STEP 1. 변수 할당
N, M = map(int, input().split())
cq = deque(i+1 for i in range(N))

target = list(map(int, input().split()))
answer = 0

# STEP 2. 하나씩 빼기
for num in target:
    index = cq.index(num)
    index_back = index - len(cq)

    if index < abs(index_back):
        answer += index
        cq.rotate(-index)
    else:
        answer += abs(index_back)
        cq.rotate(-index_back)
    cq.popleft()

print(answer)
