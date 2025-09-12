# [S2] 1912 엽속합

N = int(input())
arr = list(map(int, input().split()))

DP = arr[::]

for i in range(1, N):
    DP[i] = max(arr[i], DP[i-1] + arr[i])

print(max(DP))