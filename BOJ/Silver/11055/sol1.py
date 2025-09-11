# [S2] 11055 가장 큰 증가하는 부분 수열

N = int(input())
arr = list(map(int, input().split()))

LIS = arr[::]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            LIS[i] = max(LIS[i], LIS[j] + arr[i])

print(max(LIS))