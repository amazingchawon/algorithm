# [D2] 2001 파리퇴치

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    d = []

    # 델타탐색
    for dx in range(M):
        for dy in range(M):
            d.append([dx, dy])


    answer = arr[0][0]

    for x in range(N):
        for y in range(N):
            cnt = 0
            for dx, dy in d:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    cnt += arr[nx][ny]
            if answer < cnt:
                answer = cnt

    print(f'#{t} {answer}')