from collections import deque


def solution(maps):
    answer = -1

    # N : 지도 세로 길이, M : 지도 가로 길이
    N = len(maps)
    M = len(maps[0])

    visited = [[0]*M for _ in range(N)]
    q = deque()
    q.append((0, 0))    # 시작 위치
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        # 마지막 칸에 도착했다면 종료
        if x == N-1 and y == M-1 :
            answer = visited[N-1][M-1]
            
        # 우 하 좌 상 순으로 탐색
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            # 범위안, 방문한 적 X, 벽 X
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and maps[nx][ny] != 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
   
    return answer


input1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
input2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(input1))
print(solution(input2))