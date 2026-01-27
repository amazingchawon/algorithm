# [G5] 2225 합분해

# STEP 1. 입력 받기
N, K = map(int, input().split())

# STEP 2. DP
dp = [[0] * (K+1) for _ in range(N+1)]  # dp[n][k]: k개의 숫자로 n을 만드는 방법의 가지 수

# STEP 2.1. 초기값 세팅
for n in range(N+1):
    dp[n][1] = 1

for k in range(K+1):
    dp[0][k] = 1

# STEP 2.2. dp[N][K] 구하기
for n in range(1, N + 1):
    for k in range(2, K + 1):
        for x in range(n+1):
            dp[n][k] = (dp[n][k-1] + dp[x-1][k]) % 1000000000

print(dp[N][K])