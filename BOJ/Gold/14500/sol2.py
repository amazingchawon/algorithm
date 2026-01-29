# [G4] 14500 테트로미노

# STEP 1. 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# STEP 2. 4칸 합 구하기 (T 제외)
def dfs(x, y, depth, total):
    global res

    if depth == 4:
        res = max(res, total)
    else:
        for dx, dy in [(0, 1), (1, 0), (0, -1)]:
            tx, ty = x + dx, y + dy
            if 0 <= tx < N and 0 <= ty < M and not visited[tx][ty]:
                visited[tx][ty] = True
                dfs(tx, ty, depth + 1, total + arr[tx][ty])
                visited[tx][ty] = False

# STEP 3. T 모양 합 구하기
def check_t(x, y):
    global res

    # STEP 3.1. 세로로
    if x + 2 < N:
        vertical_sum = arr[x][y] + arr[x + 1][y] + arr[x + 2][y]
        # STEP 3.1.2. ㅓ 모양
        if 0 <= y - 1:
            res = max(res, vertical_sum + arr[x + 1][y - 1])
        # STEP 3.1.3. ㅏ 모양
        if y + 1 < M:
            res = max(res, vertical_sum + arr[x + 1][y + 1])

    # STEP 3.2. 가로로
    if y + 2 < M:
        hori_sum = arr[x][y] + arr[x][y + 1] + arr[x][y + 2]
        # STEP 3.2.1. ㅗ 모양
        if 0 <= x - 1:
            res = max(res, hori_sum + arr[x - 1][y + 1])
        # STEP 3.2.2. ㅜ 모양
        if x + 1 < N:
            res = max(res, hori_sum + arr[x + 1][y + 1])

# STEP 4. 테트로미노 최대 합 구하기
res = 0
visited = [[False] * M for _ in range(N)]

for n in range(N):
    for m in range(M):
        visited[n][m] = True
        dfs(n, m, 1, arr[n][m])
        visited[n][m] = False
        check_t(n, m)

print(res)