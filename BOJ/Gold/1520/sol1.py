# [G3] 1520 내리막 길
import sys
sys.setrecursionlimit(10**7)
# STEP 1. 입력 받기
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]

# STEP 2. DP
dp = [[-1] * N for _ in range(M)]       # dp[x][y]: (x,y)에서 (M-1,N-1)까지 가는 경로 수

# STEP 2.1. dfs로 지도 순회
def dfs(x, y):
    # STEP 2.1.1. 기본 조건
    if (x, y) == (M-1, N-1):            # 도착지에서 도착지까지 가는 경우 = 1가지
        return 1

    # STEP 2.1.2. 중복 방지
    if dp[x][y] != -1:
        return dp[x][y]

    # STEP 2.1.3. (x, y)까지 도달할 수 있는 경로의 수 계산
    dp[x][y] = 0

    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        tx, ty = x + dx, y + dy
        if 0 <= tx < M and 0 <= ty < N and arr[x][y] > arr[tx][ty]:
            dp[x][y] += dfs(tx, ty)

    return dp[x][y]


print(dfs(0, 0))