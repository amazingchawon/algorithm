# [D3] 1220 Magnetic

import sys
sys.stdin = open('input.txt', 'r')

T = 10

N, S = 1, 2

for t in range(1, T+1):
    SIZE = int(input())    # 자석판 크기, 항상 100으로 주어짐
    arr = [list(map(int, input().split())) for _ in range(SIZE)] # 자석판 만들기

    # 자석 움직이기
    for y in range(SIZE):
        while True:
            cnt = 0
            for x in range(SIZE):
                if arr[x][y] == N:                      # N극일 때,
                    if x + 1 == SIZE:                   # 자석판 제일 마지막 부분에 있다면,
                        arr[x][y] = 0                   # 자석 탈출
                    elif arr[x+1][y] == 0:              # 한 칸 아래 자석이 없다면,
                        arr[x][y], arr[x+1][y] = 0, 1   # 한 칸 아래로 이동
                        cnt += 1
                elif arr[x][y] == S:                      # S극일 때,
                    if x == 0:                          # 자석판 제일 윗 부분에 있다면,
                        arr[x][y] = 0                   # 자석 탈출
                    elif arr[x-1][y] == 0:              # 한 칸 위 자석이 없다면,
                        arr[x][y], arr[x-1][y] = 0, 1   # 한 칸 위로 이동
                        cnt += 1
            if cnt == 0:                                # 모두 탈출 or 교착상태라면
                break                                   # 다음 열로 넘어가기

    answer = 0

    # 교착 상태 수 세기
    for x in range(SIZE):
        col = ''
        for y in range(SIZE):
            col += str(arr[y][x])
        answer += col.count('12')

    print(f'#{t} {answer}')