# [D3] 11315 오목 판정

import sys
sys.stdin = open('input.txt', 'r')

def game():
    for x in range(N):
        for y in range(N):
            # 가로, 세로, 우하향 대각선, 우상향 대각선 방향으로 델타탐색
            for dx, dy in [[0, 1], [1, 1], [1, 0], [1, -1]]:
                cnt = 0
                nx, ny = x, y   # 탐색할 칸
                while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':  # 범위 안이고 돌이 놓여있다면
                    cnt += 1 # 돌 카운트 수 늘려주기
                    nx += dx # 다음 탐색할 칸으로 이동
                    ny += dy # 다음 탐색할 칸으로 이동
                    if cnt == 5: # 5개 채웠을 경우
                        return 'YES'
    return 'NO'

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    answer = game()   # 출력할 값, NO로 초기화

    print(f'#{t} {answer}')