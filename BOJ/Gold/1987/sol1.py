# [G4] 알파벳

def dfs(x, y, count):
    global answer
    answer = max(answer, count)

    for i in range(4):

        nx = dx[i] + x
        ny = dy[i] + y

        if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
            continue

        if visited[ord(arr[nx][ny]) - 65] == 0:
            visited[ord(arr[nx][ny]) - 65] = 1
            dfs(nx, ny, count+1)
            visited[ord(arr[nx][ny]) - 65] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

visited = [0] * 26
visited[ord(arr[0][0])-65] = 1

answer = 1

dfs(0, 0, 1)

print(answer)