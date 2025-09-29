# [G5] 12865 평범한 배낭

import sys
input = sys.stdin.readline

# STEP 1. 입력 받기
N, K = map(int, input().split())    # N: 물품의 수, K: 버틸 수 있는 최대 무게
items = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]  # items: 각 아이템의 [무게, 가치] 정보를 저장 (1-indexed로 사용하기 위해 [0,0] 추가)

dp = [[0] * (K + 1) for _ in range(N + 1)]  # dp[i][k]: i번째 물건까지 고려했을 때, 무게 k 이하로 담을 수 있는 최대 가치

# STEP 2. DP 구현
for i in range(1, N + 1):           # i번째 아이템을 고려할때,
    w, v = items[i]                 # 현재 아이템의 무게와 가치
    for k in range(1, K + 1):       # 가능한 무게 k를 1부터 K까지 순회
        if k < w:                   # 현재 무게 k로는 이 물건을 담을 수 없을 때,
            # 이전 상태 그대로 사용
            dp[i][k] = dp[i - 1][k]
        else:                       # 담을 수 있을 때
            # 이 물건을 담을 수 있음 → 담지 않았을 때 vs 담았을 때 중 최대값 선택
            # 담았을 경우: 이전 아이템까지 고려했을 때 무게 (k - w) 이하로 담을 수 있는 최대 가치에 현재 가치 v 더함
            dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - w] + v)

print(dp[N][K])
