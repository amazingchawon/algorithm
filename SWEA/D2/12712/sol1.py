# [D2] 12712 파리퇴치 3

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    # N : 배열 크기, M : 스프레이 강도
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    for x in range(N):
        for y in range(N):
            tmp = arr[x][y]         # 죽은 파리 개체 수 저장 변수
            # + 자로 스프레이 뿌리기
            for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                for i in range(1, M):   # i : 스프레이의 범위
                    nx = x + dx * i
                    ny = y + dy * i
                    if 0 <= nx < N and 0 <= ny < N:
                        tmp += arr[nx][ny]
            if answer < tmp:
                answer = tmp
            # x 자로 스프레이 뿌리기
            tmp = arr[x][y]         # 죽은 파리 개체 수 저장 변수
            for dx, dy in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
                for i in range(1, M):
                    nx = x + dx * i
                    ny = y + dy * i
                    if 0 <= nx < N and 0 <= ny < N:
                        tmp += arr[nx][ny]
            if answer < tmp:
                answer = tmp

    print(f'#{t} {answer}')