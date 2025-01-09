# [S3] 2579 계단 오르기

import sys

N = int(sys.stdin.readline())
steps = [0] * N
dp = [0] * N

for n in range(N):
    steps[n] = int(sys.stdin.readline())
    if n == 0:
        dp[n] = steps[0]
    elif n == 1:
        dp[n] = steps[0] + steps[1]
    else:
        # 연속해서 3칸 밟기 금지
        # 경우 1 : 내 직전 칸을 밟지 않았을 경우 -> 두 칸 아래의 최대 값 + 내 지금 계단 값
        # 경우 2 : 내 직전 칸을 밟았을 경우 -> 세 칸 아래의 최대 값 + 한 칸 아래 값 + 내 지금 계단 값
        # 내 직전 칸의 dp 값이 이미 연속해서 밟은 결과일수도 -> dp[n-1]이 아니라 steps[n-1]인 이유
        dp[n] = max(dp[n-2] + steps[n], dp[n-3] + steps[n-1] + steps[n])

print(dp[-1])   # 맨 마지막 계단 꼭 밟아야 함
