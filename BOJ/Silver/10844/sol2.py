# [S1] 10844 쉬운 계단 수

N = int(input())

dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
MOD = 10**9

for _ in range(1, N):
    new_dp = [0] * 10
    new_dp[0] = dp[1]
    new_dp[9] = dp[8]

    for i in range(1, 9):
        new_dp[i] = (dp[i-1] + dp[i+1]) % MOD
    dp = new_dp

answer = sum(dp) % MOD
print(answer)