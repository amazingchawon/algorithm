# [G5] 7576 토마토

from collections import deque

# STEP 1. 입력 받기
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
day = 0

# STEP 2. 토마토 익히기
tomato = deque()

# STEP 2-1. 익은 토마토 찾기
for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:          # 익은 토마토 찾아서
            tomato.append((x, y))   # 위치 넣어주기

while tomato:
    for _ in range(len(tomato)):
        x, y = tomato.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            tx = x + dx
            ty = y + dy
            if 0 <= tx < N and 0 <= ty < M and arr[tx][ty] == 0:
                arr[tx][ty] = 1
                tomato.append((tx, ty))
    day += 1

for x in range(N):
    for y in range(M):
        if arr[x][y] == 0:
            day = -1
            break
    if day == -1:
        break

print(day -1 if day > 0 else day)