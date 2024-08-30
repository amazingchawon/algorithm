# [D4] 10966 물놀이를 가자

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())    # N*M 배열
    arr = [input() for _ in range(N)]

    answer = 0                          # 출력할 변수

    # STEP 1. W 좌표 찾기
    check = sum([row.count('W') for row in arr])              # W의 수
    coordinate_w = [0] * check          # W 좌표 기록할 배열. [Wx, Wy]
    cnt = 0                             # arr 순회 종료를 위한 변수, 여태까지 발견한 W의 개수를 세는 변수

    for x in range(N):
        for y in range(M):
            if cnt == check:
                break
            else:
                if arr[x][y] == 'W':
                    coordinate_w[cnt] = [x, y]
                    cnt += 1
        if cnt == check:
            break

    # STEP 2. 거리 구하기
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 'L':        # L 찾으면,
                min_d = N + M
                for wx, wy in coordinate_w: # W 좌표들과 거리 차이 구하기
                    # tmp = |wx-x| + |wy-y|
                    if wx > x :
                        tmp = wx -x
                    else:
                        tmp = x - wx
                    if wy > y:
                        tmp += wy -y
                    else:
                        tmp += y - wy
                    # 현재 L에서 제일 가까운 W인지 확인
                    if min_d > tmp:
                        min_d = tmp
                answer += min_d

    print(f'#{t} {answer}')