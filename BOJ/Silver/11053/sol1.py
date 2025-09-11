# [S2] 11053 가장 긴 증가하는 부분 수열

N = int(input())
arr = list(map(int, input().split()))

DP = [1] * N

for i in range(N):
    for j in range(0, i):
        if arr[i] == arr[j]:
            DP[i] = DP[j]
        elif arr[i] > arr[j]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))