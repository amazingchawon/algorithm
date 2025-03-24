# [S1] 1149 RGB 거리

# STEP 1. 입력 받기
N = int(input())
arr = [0] * N

# STEP 2. 한 줄 씩 (i번쨰 집의) 페인트 비용 받아오기
for i in range(N):
    arr[i] = list(map(int, input().split()))

# STEP 3. 최소 비용 찾기
for i in range(1, N):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1]
    arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2]

print(min(arr[N-1][0], arr[N-1][1], arr[N-1][2]))