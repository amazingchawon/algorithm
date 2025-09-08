# [S3] 2193 이친수
N = int(input())

DP = [0, (0, 1), (1, 0)] + [0] * 88

for i in range(3, N+1):
    ends_with_zero, ends_with_one = DP[i-1]
    DP[i] = (ends_with_zero + ends_with_one, ends_with_zero)

answer = DP[N][0] + DP[N][1]
print(answer)