# [G5] 21758 꿀따기
# 실패

import sys

# STEP 1. 입력 받기
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0

# STEP 2. 최대값 계산

# CASE 1. 벌1 벌2 벌통
# 벌 위치 <-> 벌집 위치가 최대인 것이 최적해
# 벌 위치를 (0, 1) -> (0, N-2) 이동해보면서 최대값 찾기

for i in range(1, N-1):         # i는 벌2의 위치
    tmp = sum(arr[1:i]) + sum(arr[i+1:]) * 2
    answer = max(answer)

# CASE 2. 벌통 벌1 벌2
for j in range(N-2, 0, -1):     # j는 벌1의 위치
    tmp = 2 * sum(arr[0:j]) + sum(arr[j+1: N-1])
    if answer < tmp:
        answer = tmp

# CASE 3. 벌 벌통 벌
for k in range(1, N-1):     # k는 벌통의 위치
    tmp = sum(arr[1:k+1]) + sum(arr[j:N-1])
    if answer < tmp:
        answer = tmp

print(answer)