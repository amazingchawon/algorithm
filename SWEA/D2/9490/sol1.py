# [D2] 9490 풍선팡

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_flower = arr[0][0]

    # arr 순회
    for x in range(N):
        for y in range(M):
            flower = arr[x][y]                                  # 현재 칸에 든 풍선의 꽃가루 양
            cnt = flower                                        # 현재 칸에서 얻을 수 있는 총 꽃가루의 양을 저장할 변수
            for power in range(1, flower+1):
                for i, j in [[1,0], [-1, 0], [0, 1], [0, -1]]:  # 상하좌우 탐색
                    nxt_x = x + i * power
                    nxt_y = y + j * power
                    if 0 <= nxt_x < N and 0 <= nxt_y < M:        # 범위체크
                        cnt += arr[nxt_x][nxt_y]
            if max_flower < cnt:                                # 현재까지 최대 꽃가루 양이 현재 칸의 꽃가루가 크다면
                max_flower = cnt                                # 갱신

    print(f'#{t} {max_flower}')