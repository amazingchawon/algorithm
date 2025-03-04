# [G5] 적록색약

from collections import deque

def BFS(x, y):
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            # 인덱스 범위 안, 같은 색, 방문 안한 경우
            if 0 <= nx < N and 0 <= ny < N and arr[x][y] == arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))


# STEP 1. 입력 받기
N = int(input())
arr = [list(input()) for _ in range(N)]

q = deque()

# STEP 2. 적록 색약이 아닐 경우
visited = [[0] * N for _ in range(N)]
cnt1 = 0
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            BFS(x, y)
            cnt1 += 1

# STEP 3. 적록 색약일 경우
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
cnt2 = 0
for x in range(N):
    for y in range(N):
        if not visited[x][y]:
            BFS(x, y)
            cnt2 += 1

print(cnt1, cnt2)