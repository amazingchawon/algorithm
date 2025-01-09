# [S2] 11722 가장 긴 감소하는 부분 수열

import sys

# 반례
# 7
# 5 3 4 8 6 7 2

# STEP 1. 입력 받기
N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

# STEP 2. arr 순회 -> 최장 감소 부분 수열 구하기
LDS = [1] * N
for i in range(1, N):                                       # i번째 수 보기
    tmp = 1                                                 # i번째 수에서
    for j in range(i-1, -1, -1):                            # i-1 번째부터 0번째까지 순회
        if arr[i] < arr[j] and tmp <= LDS[j]:               # i번째 수가 j번째 수보다 크다면
            tmp = LDS[j] + 1                                # LDS 크기 1 증가
        # 틀린 이유 : 이 코드가 불필요 했음
        elif arr[i] >= arr[j] and tmp <= LDS[j]:            # i번째 수가 j번째 수보다 작거나 같다면
            tmp = LDS[j]
    LDS[i] = tmp

print(max(LDS))