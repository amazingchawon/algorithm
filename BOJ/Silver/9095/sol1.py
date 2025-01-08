# [S3] 9095 1, 2, 3 더하기

import sys

T = int(sys.stdin.readline())

memo = [0] * 12

for i in range(1, 12):
    if i == 1:
        memo[i] = 1
    elif i == 2:
        memo[i] = 2
    elif i == 3:
        memo[i] = 4
    else:
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

for t in range(T):
    n = int(sys.stdin.readline())
    print(memo[n])