# [S3] 9461 파도반 수열

T = int(input())
DP = [0, 1, 1, 1] + [0] * 97

for n in range(4, 101):
    DP[n] = DP[n-2] + DP[n-3]

for _ in range(T):
    N = int(input())

    print(DP[N])