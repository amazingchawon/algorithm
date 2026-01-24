# [G4] 14226 이모티콘

from collections import deque

# STEP 1. 입력 받기
S = int(input())
MAX = 2 * S

q = deque()
q.append((0, 1, 0))                             # (소요시간, 이모지 개수, 복사창)
visited = [[False] * MAX for _ in range(MAX)]   # visited[x][y]: 화면 이모티콘 수 x, 클립보드 이모티콘 수 y
visited[1][0] = 1

while True:
    time, screen, clip = q.popleft()

    if screen == S:
        print(time)
        break

    # STEP 2.2. 이모티콘 복사
    ns, nc = screen, screen
    if 0 <= ns < MAX and 0 <= nc < MAX and not visited[ns][nc]:
        visited[ns][nc] = True
        q.append((time + 1, ns, nc))

    # STEP 2.2. 붙여넣기
    if clip > 0:
        ns, nc = screen + clip, clip
        if 0 <= ns < MAX and 0 <= nc < MAX and not visited[ns][nc]:
            visited[ns][nc] = True
            q.append((time + 1, ns, nc))

    # STEP 2.3. 삭제
    if screen > 0:
        ns, nc = screen - 1, clip
        if 0 <= ns < MAX and 0 <= nc < MAX and not visited[ns][nc]:
            visited[ns][nc] = True
