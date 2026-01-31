# [G4] 2573 빙산

# STEP 1. 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
year = 0

# STEP 2. dfs
def dfs(x, y):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny]:                 # 빙산이라면,
                    stack.append((nx, ny))      # 스택에 추가 -> 빙산 덩어리 탐색
                    visited[nx][ny] = True
    return 1

# STEP 3. 빙산 주변 바다 세기 + 녹이기
def melt_ice(ice):

    # STEP 3.1. 빙산 주변 바다 세기
    for x, y in ice:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                sea[x][y] += 1

    # STEP 3.2. 녹이기
    new_ice = []
    for x, y in ice:
        new_height = max(arr[x][y] - sea[x][y], 0)
        arr[x][y] = new_height
        if new_height > 0:
            new_ice.append((x, y))

    return new_ice

# STEP 4. 구현
# STEP 4.1. 초기 얼음 위치 세팅
ice = []
for n in range(N):
    for m in range(M):
        if arr[n][m] > 0:
            ice.append((n, m))

while True:
    # STEP 4.2.1. 빙산 그룹 갯수 확인
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    sea = [[0] * M for _ in range(N)]

    for x in range(N):
        for y in range(M):
            if arr[x][y] and not visited[x][y]:
                cnt += dfs(x, y)

    if cnt > 1:
        break
    elif cnt == 0:
        year = 0
        break

    # STEP 4.2.2. 빙산 녹이기
    ice = melt_ice(ice)

    if len(ice) == 0:
        year = 0
        break

    # STEP 4.2.3. 한해 보내기
    year += 1

print(year)