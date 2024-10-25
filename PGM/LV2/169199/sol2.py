def solution(board):
    row_cnt = len(board)
    col_cnt = len(board[0])

    # STEP 1. 시작 위치 찾기
    start = None
    for r in range(row_cnt):
        for c in range(col_cnt):
            if board[r][c] == 'R':
                start = (r, c)
                break
        if start != None:
            break

    # STEP 2. BFS 이용 최소 회수 찾기
    q = [start]
    visited = [[-1] * col_cnt for _ in range(row_cnt)]
    visited[start[0]][start[1]] = 0

    # 상, 우, 하, 좌 방향
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while q:
        x, y = q.pop(0)

        if board[x][y] == 'G':
            return visited[x][y]

        for dx, dy in directions:
            nx, ny = x, y

            # 벽이나 장애물에 닿기 전까지 가기
            while 0 <= nx+dx < row_cnt and 0 <= ny+dy < col_cnt and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy

            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return -1


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])) # 7
print(solution([".D.R", "....", ".G..", "...D"])) # -1