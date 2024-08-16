# [D2] 16268 풍선팡2

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())    # N X M 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = arr[0][0]

    for x in range(N):
        for y in range(M):
            cnt = arr[x][y]
            for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    cnt += arr[nx][ny]
            if max_cnt < cnt:
                max_cnt = cnt

    print(f'#{t} {max_cnt}')