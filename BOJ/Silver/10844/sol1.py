# [S1] 10844 쉬운 계단 수

N = int(input())

DP = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]] + [[0] * 10 for _ in range(N-1)]

for i in range(1, N):
    DP[i][0] = DP[i-1][1]
    DP[i][9] = DP[i-1][8]

    for num in range(1, 9):
        DP[i][num] = DP[i-1][num-1] + DP[i-1][num+1]

answer = sum(DP[N-1]) % 1000000000
print(answer)