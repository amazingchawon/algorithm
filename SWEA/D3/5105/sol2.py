# [D3] 5105 미로의 거리

import sys
sys.stdin = open('input.txt', 'r')


def BFS(start):
    global result

    queue = [start]

    while queue:
        tx, ty = queue.pop(0)

        # 종료 조건
        if maze[tx][ty] == 3:
            result = visited[tx][ty] - 1
            return

        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nx = tx + dx
            ny = ty + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and maze[nx][ny] != 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[tx][ty] + 1


T = int(input())

for t in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # STEP 1. 시작점(2) 찾기
    for x in range(N):
        for y in range(N):
            if maze[x][y] == 2:
                S = (x, y)

    # STEP 2. 미로 BFS 탐색
    result = 0
    visited = [[0] * N for _ in range(N)]
    BFS(S)

    print(f'#{t} {result}')