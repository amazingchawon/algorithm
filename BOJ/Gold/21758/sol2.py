# [G5] 21758 꿀따기

import sys
from copy import deepcopy

# STEP 1. 입력 받기
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0

# STEP 2. 합 미리 계산
s = deepcopy(arr)
for i in range(1, N):
    s[i] += s[i-1]

# STEP 2. 최대값 계산

# CASE 1. 벌1 벌2 벌통
for i in range(1, N-1):                 # i는 벌2의 위치
    bee1 = s[-1] - arr[0] - arr[i]      # 벌 1이 따는 꿀 수
    bee2 = s[-1] - s[i]                 # 벌 2가 따는 꿀 수
    answer = max(answer, bee1+bee2)

# CASE 2. 벌통 벌1 벌2
for i in range(1, N-1):                 # j는 벌1의 위치
    bee1 = s[i - 1]                     # 자기 위치 직전까지 누적합
    bee2 = s[-1] - arr[-1] - arr[i]     # 전체 누적합 - 벌1 위치 - 자기 위치
    answer = max(answer, bee1+bee2)

# CASE 3. 벌 벌통 벌
for i in range(1, N-1):     # k는 벌통의 위치
    bee1 = s[i] - arr[0]                    # 꿀까지 누적합 - 자기 위치
    bee2 = s[-1] - s[i-1] - arr[-1]         # 전체 누적합 - 꿀까지 누적합 - 자기 위치
    answer = max(answer, bee1+bee2)

print(answer)