# [D4] 10966 물놀이를 가자

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())    # N*M 배열
    arr = [list(input()) for _ in range(N)]

    answer = 0                          # 출력할 변수

    # DFS로 풀기
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 'L':
                nx, ny = x, y
                stack = [[nx, ny]]
                while True:
                    for nx, ny in stack:

                        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                            nx = x + dx
                            ny = y + dy
                            if 0 <= nx < N and 0 <= ny < M:                 # 범위 안이면,
                               stack.append([nx, ny])                       # 방문할 곳에 추가

    print(f'#{t} {answer}')