# [D3] 5105 미로의 거리

import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def BFS(start, end, arr):
    visited = [[0] * N for _ in range(N)]  # 방문 횟수 저장 배열
    queue = []  # 큐생성
    queue.append(start)
    visited[start[0]][start[1]] = 1
    while queue:
        current = queue.pop(0)
        for i in range(4):
            nxt_x = current[0] + dx[i]
            nxt_y = current[1] + dy[i]
            if 0 <= nxt_x < N and 0 <= nxt_y < N and arr[nxt_x][nxt_y] == 0 and visited[nxt_x][nxt_y] == 0:  # arr 범위 안이고, 길이고, 방문하지 않은 곳이면,
                queue.append([nxt_x, nxt_y])
                visited[nxt_x][nxt_y] = visited[current[0]][current[1]] + 1  # 직전 정점에서 이동 횟수 하나 늘려주기 = 현재 정점 올때까지 걸리는 횟수
            if 0 <= nxt_x < N and 0 <= nxt_y < N and arr[nxt_x][nxt_y] == 3: # 종점에 도착
                if visited[nxt_x][nxt_y] != 0:                  # 종점을 이미 방문했었던거라면
                    tmp = visited[current[0]][current[1]] + 1   # 현재 루트로 종점을 방문한다면 걸리는 횟수가
                    if visited[nxt_x][nxt_y] < tmp:             # 기존에 기록된 것보다 크다면,
                        pass                                    # 패스
                    else:                                       # 기존에 기록된 것보다 작다면
                        visited[nxt_x][nxt_y] = tmp             # 갱신
                else:
                    visited[nxt_x][nxt_y] = visited[current[0]][current[1]] + 1

    return visited[end[0]][end[1]]


T = int(input())  # 테스트 케이스 수

for t in range(1, T + 1):
    N = int(input())  # 미로 크기
    maze = [list(map(int, input())) for _ in range(N)]  # 미로

    # 시작점과 끝점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
            elif maze[i][j] == 3:
                end = [i, j]

    answer = BFS(start, end, maze)

    if answer > 0:
        answer -= 2

    print(f'#{t} {answer}')