# [S1] 1463 1로 만들기

N = int(input())

DP = [0] * (10**6 + 1)  # 메모이제이션

for i in range(2, N+1):
    # 경우 1. -1
    DP[i] = DP[i-1] + 1
    # 경우 2. 2로 나누어 지는 경우
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i//2] + 1)
    # 경우 3. 3으로 나누어 지는 경우
    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i//3] + 1)

print(DP[N])