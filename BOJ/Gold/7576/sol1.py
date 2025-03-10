# [G5] 7576 토마토
# 시간초과

# STEP 1. 입력 받기
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# STEP 2. 불가능한 경우가 있는지 판단
repeat = True
answer = 0

for x in range(N):
    for y in range(M):
        if arr[x][y] == 0:
            tmp = 0
            cnt = 0
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                tx = x + dx
                ty = y + dy
                if 0 <= tx < N and 0 <= ty < M:
                    tmp += 1
                    if arr[tx][ty] == -1:
                        cnt += 1
            if tmp == cnt:
                repeat = False
                answer = -1
                break
    if answer == -1:
        break

# STEP 3. 토마토가 언제 익을까
tomato = 1
while repeat:
    check = 0                   # 0인 자리가 하나도 없는지 감시
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 0:
                check += 1      # 0인 토마토 있음!
                for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    tx = x + dx
                    ty = y + dy
                    if 0 <= tx < N and 0 <= ty < M and arr[tx][ty] == tomato:       # 인접한 칸에 익은 토마토 있으면
                        arr[x][y] = tomato + 1      # 이 토마토도 익히기! (+1을 해주어 날이 안지났는데도 적용되는걸 막는다)
                        break
    if check:
        tomato += 1
        answer += 1
    else:
        repeat = False
        break

print(answer)