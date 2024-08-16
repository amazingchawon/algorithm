# [D3] 11315 오목 판정

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    answer = 'NO'   # 출력할 값, NO로 초기화

    for x in range(N):
        for y in range(N):
            if arr[x][y] == 'o':    # 현재 칸에 돌이 놓여있다면,
                cnt = 0
                # 가로, 세로, 우하향 대각선, 우상향 대각선 방향으로 델타탐색
                for dx, dy in [[0, 1], [1, 1], [1, 0], [1, -1]]:
                    cnt = 1
                    for i in range(1, 5):
                        nx, ny = x + dx*i, y + dy*i # 다음 탐색 칸
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':  # 범위 안이고 돌이 놓여있다면
                            cnt += 1
                        else:
                            break
                    if cnt == 5: # 오목 조건이 맞다면
                        answer = 'YES'
                        break
        if answer == 'YES':
            break

    print(f'#{t} {answer}')