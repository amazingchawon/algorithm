# [S3] 1021 회전하는 큐

import sys
input = sys.stdin.readline

# STEP 1. 변수 할당
N, M = map(int, input().split())
cq = [i+1 for i in range(N)]

target = list(map(int, input().split()))
answer = 0

# STEP 2. 하나씩 빼기
for num in target:
    index = cq.index(num)
    index_back = index - len(cq)

    left = index
    right = abs(index - len(cq))

    answer += min(left, right)
    cq = cq[index + 1:] + cq[:index]

print(answer)
