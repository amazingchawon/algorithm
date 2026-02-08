# [G4] 17404 RGB거리 2

# STEP 1. 입력받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

INF = 10**8
answer = INF

dp = [[INF, INF, INF] for _ in range(N)]

dp[0] = [arr[0][0], INF, INF]

for i in range(1, N):
    dp[i][0] = arr[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1])

answer = min(dp[N - 1][1], dp[N - 1][2])

dp = [[INF, INF, INF] for _ in range(N)]

dp[0] = [INF, arr[0][1], INF]

for i in range(1, N):
    dp[i][0] = arr[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1])

answer = min(answer, dp[N - 1][0], dp[N - 1][2])

dp = [[INF, INF, INF] for _ in range(N)]

dp[0] = [INF, INF, arr[0][2]]

for i in range(1, N):
    dp[i][0] = arr[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = arr[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = arr[i][2] + min(dp[i - 1][0], dp[i - 1][1])

answer = min(answer, dp[N - 1][0], dp[N - 1][1])

print(answer)
