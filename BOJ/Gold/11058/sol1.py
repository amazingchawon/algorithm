# [G5] 11058 크리보드

N = int(input())

DP = [num for num in range(N+1)]

for i in range(7, N+1):
    for j in range(0, i - 2):
        DP[i] = max(DP[i-3-j] * (2 + j), DP[i])

print(DP[N])