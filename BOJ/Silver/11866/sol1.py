# [S4] 11866 요세푸스 문제 0

import sys
input = sys.stdin.readline

# STEP 1. 입력 받기
N, K = map(int, input().split())
q = [i for i in range(1, N+1)]

result = []

# STEP 2. 순환
cnt = 1
index = 0

while q:
    if index == len(q):
        index = 0

    if cnt == K:
        result.append(q.pop(index))
        cnt = 1
    else:
        cnt += 1
        index += 1

print('<' + ', '.join(map(str, result)) + '>')