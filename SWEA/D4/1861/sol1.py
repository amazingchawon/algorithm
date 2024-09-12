# [D4] 1861 정사각형 방

import sys
sys.stdin = open('input.txt', 'r')

def DFS(V):
    stack = [V]

    while stack:
        x, y = stack.pop()
        visited[x][y] = 1
        for dx, dy in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[x][y] + 1 == arr[nx][ny]:
                stack.append((nx, ny))
                level[nx][ny] = level[x][y] + 1
                break                   # 숫자가 모두 다르므로, 한 방향으로 밖에 탐색 불가

    return level[x][y]


T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    room_num = 0
    max_move = 0
    level = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]   # 가지치기 용 : 이전 순회에서 지나간 곳이라면, 거기서 시작하는게 지나가는 방의 개수가 무조건 작을 수 밖에 없음

    for i in range(N):
        for j in range(N):
            if visited[i][j]:               # 이미 지나간 곳이 시작점이 될 필요 X, 따라서 PASS
                continue
            level[i][j] = 1
            tmp_room, tmp_move = arr[i][j], DFS((i, j))
            if max_move < tmp_move:                 # 최대 움직인 방 수 보다 현재 위치에서 움직인 방 수가 더 많으면,
                room_num = tmp_room                 # 움직인 방 번호 갱신
                max_move = tmp_move                 # 최대 움직인 방 수 갱신
            elif max_move == tmp_move:              # 동일하다면,
                room_num = min(room_num, tmp_room)  # 움직인 방 번호 중 작은 걸로 갱신 (이거 안해줘도 되긴함)

    print(f'#{t} {room_num} {max_move}')