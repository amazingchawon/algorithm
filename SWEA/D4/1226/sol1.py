# [D4] 1226 미로1

import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(10):
    N = int(input())    # N : 문제 번호
    maze = [list(map(int, input())) for _ in range(16)]

    answer = 0      # 출력할 답, 불가능으로 초기화
    start = [1, 1]  # 시작 포인트
    move = [start]  # 이동할 곳을 담은 큐
    history = []     # 지나온 곳을 담을 리스트

    while move:
        current = move.pop(0)       # 현재 위치
        history.append(current)     # 지나온 곳 리스트에 추가
        # 현재 위치에서 갈 수 있는 곳 탐색
        for i in range(4):
            nxt_x = current[0]+dx[i]
            nxt_y = current[1]+dy[i]
            tmp = maze[nxt_x][nxt_y]  # 델타 탐색
            if tmp == 0 and [nxt_x, nxt_y] not in history:    # 갈 수 있는 곳이라면,
                move.append([nxt_x, nxt_y])
            elif tmp == 3:  # 목적지라면,
                answer = 1
                break

    print(f'#{N} {answer}')