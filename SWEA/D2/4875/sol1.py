# [D2] 4875 미로

import sys
sys.stdin = open('input.txt', 'r')

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

"""
delta의 다른 방법
for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
"""

def search(x, y):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로의 범위를 벗어나지 않았는지
            # maze에서 벽이 아닌지, 방문한적이 없는지
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != '1' and visited[nx][ny] == 0:
                if maze[nx][ny] == '3':   # 출구 도착
                    return 1            # 1 반환 후 함수 종료
                # 3이 아니라면
                stack.append((nx, ny))

    return 0

T = int(input())

for t in range(1, T+1):
    N = int(input())

    maze = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                print(f'#{t} {search(i, j)}')