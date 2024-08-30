# [D4] 10966 물놀이를 가자

import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for dx, dy in [[-1,0], [1, 0], [0, -1], [0, 1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())    # N*M 배열
    arr = [list(input()) for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]

    q = deque()

    # STEP 1. 물 찾기
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                q.append([i, j])
                visited[i][j] = 0

    # STEP 2. BFS

    print(f'#{t} {answer}')