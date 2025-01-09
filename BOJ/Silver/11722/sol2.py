# [S2] 11722 가장 긴 감소하는 부분 수열

import sys

# STEP 1. 입력 받기
N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

# STEP 2. arr 순회 -> 최장 감소 부분 수열 구하기
LDS = [1] * N
for i in range(1, N):                                       # i번째 수 보기
    for j in range(i-1, -1, -1):                            # i-1 번째부터 0번째까지 순회
        if arr[i] < arr[j]:
            LDS[i] = max(LDS[i], LDS[j]+1)

print(max(LDS))