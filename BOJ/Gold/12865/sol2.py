# [G5] 12865 평범한 배낭

import sys
input = sys.stdin.readline

# STEP 1. 입력 받기
N, K = map(int, input().split())
items = [(map(int, input().split())) for _ in range(N)] # (무게, 가치) 저장

dp = [0] * (K+1)    # dp[k] : k 무게일 때 가치 최대 값

# STEP 2. 물건 담기
for w, v in items:
    for k in range(K, w-1, -1): # 최대 무게부터 현재 아이템의 무게 까지
        dp[k] = max(dp[k], dp[k-w] + v)

print(dp[K])