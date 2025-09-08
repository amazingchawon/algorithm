# [S3] 11727 2xn 타일링 2

n = int(input())
DP = [0, 1, 3] + [0] * 998

for i in range(3, n + 1):
    DP[i] = (DP[i-1] + DP[i-2] * 2) % 10007

print(DP[n])