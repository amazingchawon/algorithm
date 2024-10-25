def solution(board):
    answer = -1

    row_cnt = len(board)
    col_cnt = len(board[0])

    # STEP 1. 시작 위치 찾기
    start = False
    for r in range(row_cnt):
        for c in range(col_cnt):
            if board[r][c] == 'R':
                start = (r, c)
                break
        if start != False:
            break

    # STEP 2. BFS 이용 최소 회수 찾기
    q = [start]
    visited = [[0] * col_cnt for _ in range(row_cnt)]
    checked = []
    while q:
        x, y = q.pop(0)
        if board[x][y] == 'G':
            answer = visited[x][y]
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            while 0 <= nx < row_cnt and 0 <= ny < col_cnt:
                if board[nx][ny] == '.' or board[nx][ny] == 'G':
                    if visited[nx][ny] != 0 and visited[nx][ny] <= visited[x][y]:
                        break
                    visited[nx][ny] = visited[x][y] + 1
                elif board[nx][ny] == 'D':
                    check = (nx-dx, ny-dy)
                    if check not in checked:
                        q.append((nx-dx, ny-dy))
                        checked.append(check)
                    break
                nx += dx
                ny += dy
    return answer


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])) # 7
print(solution([".D.R", "....", ".G..", "...D"])) # -1