# [G4] 2573 빙산

# STEP 1. 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

year = 0

# STEP 2. 빙하 덩어리를 세기 위한 dfs 정의
def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        cx, cy = stack.pop()
        ice.append((cx, cy))    # 빙하 있는 곳 기록

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))

    return 1

# STEP 3. 빙하 녹이는 함수 정의
def melt_ice(ice_cube):
    # STEP 3.1. 각 빙하 주의에 몇개의 바다가 있는지 카운트
    for x, y in ice_cube:
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    sea[x][y] += 1

    # STEP 3.2. 빙하 녹이기
    new_ice = []
    for x, y in ice_cube:
        tmp = max(arr[x][y] - sea[x][y], 0)
        arr[x][y] = tmp
        if tmp:                     # 아직 빙하가 남아있다면,
            new_ice.append((x, y))  # 빙하 목록에 넣어주기

    return new_ice


# STEP 4. 로직 작성
while True:
    # STEP 4.1. 빙하 덩어리 세기
    visited = [[False] * M for _ in range(N)]
    ice = []
    sea = [[0] * M for _ in range(N)]

    cnt = 0

    for n in range(1, N-1):
        for m in range(1, M-1):
            if arr[n][m] and not visited[n][m]:
                cnt += dfs(n, m)

    if cnt > 1:
        break
    elif cnt == 0:
        year = 0
        break

    # STEP 4.2. 빙하 녹이기
    ice = melt_ice(ice)

    if len(ice) == 0:
        year = 0
        break

    year += 1

print(year)