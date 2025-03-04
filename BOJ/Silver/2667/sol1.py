# [S1] 단지번호붙이기

from collections import deque

# STEP 0. BFS
def bfs(arr, x, y):
    n = len(arr)
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count

# STEP 1. 입력 받기
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

answer = []

# STEP 2. 순회
for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:
            answer.append(bfs(arr, x, y))

answer.sort()
print(len(answer))
for num in answer:
    print(num)