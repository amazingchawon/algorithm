# [A형 기출] 5656 벽돌깨기

import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def shoot(level, remains, bricks):
    global min_left

    # 기저 조건
    # 구슬을 모두 발사 or 남은 벽돌이 0이면 종료
    if level == N or remains == 0:
        min_left = min(min_left, remains)   # 최소값 갱신
        return

    # 벽돌 깨기
    # 1. 한 줄씩 쏘기
    for col in range(W):
        # 방법 1.
        # 1. col 위치에 쏘기 전 상태를 복사
        # 2. 원본 리스트의 col 위치에 구슬을 쏜다
        # 3. level + 1 상태로 이동 (다음 재귀 호출)
        # 4. col 위치에 쏘기 전 상태로 복구
        # 방법 2. (복구하는 시간이 너무 오래 걸림)
        # 1. col 위치에 쏘기 전 상태를 복사
        # 2. 복사한 리스트의 col 위치에 구슬을 쏜다
        # 3. level + 1 상태로 이동 (다음 재귀 호출) -> 복사한 리스트 전달
        bricks_copy = [row[:] for row in bricks]

        # 2. col 위치에서 구슬 쏘기
        # (1) 구슬 쏘는 열에서 가장 위에 있는 벽돌 찾기
        row = -1
        for r in range(H):
            if bricks_copy[r][col]:
                row = r
                break
        if row == -1:       # 벽돌이 없는 열 -> 다음 열로 넘어가자
            continue

        # (2) 연쇄적으로 벽돌이 깨짐
        li = [(row, col, bricks_copy[row][col])]    # 깨져야할 벽돌들을 저장 : (행, 열, 파워)
        now_remains = remains - 1
        bricks_copy[row][col] = 0

        while li:
            x, y, power = li.pop()
            for k in range(1, power):   # 파워만큼 퍼지면서 깨짐
                for i in range(4):      # 상하좌우
                    nx = x + (dx[i] * k)
                    ny = y + (dy[i] * k)

                    if nx < 0 or nx >= H or ny < 0 or ny >= W:
                        continue

                    if bricks_copy[nx][ny] == 0:    # 벽돌이 없다면 통과
                        continue

                    li.append((nx, ny, bricks_copy[nx][ny]))
                    bricks_copy[nx][ny] = 0
                    now_remains -= 1

        # 2. 떨어트리기 (중력)
        gravity(bricks_copy)
        shoot(level + 1, now_remains, bricks_copy)


def gravity(arr):
    for c in range(W):  # 떨어트릴 열 가져오기
        idx = H - 1  # 벽돌이 위치할 index
        for r in range(H - 1, -1, -1):
            if arr[r][c]:  # 벽돌이 이미 있다면
                # idx와 row가 같아도 바꾼다 == 의미없는 교환
                # 가독성을 위해 아래와 같이 구현
                arr[r][c], arr[idx][c] = arr[idx][c], arr[r][c]
                idx -= 1


T = int(input())

for t in range(1, T+1):
    N, W, H = map(int, input().split())                             # N : 벽돌 깨는 횟수
    arr = [list(map(int, input().split())) for _ in range(H)]       # W * H 배열

    # 1. 최소 벽돌
    #  - 몇개 남았을까 계산해야한다 -> 2차원 리스트를 순회하면서 매 번 계산하면 너무 느리다
    #  - 현재 남은 벽돌 수를 저장 -> 해결!
    # 2. 남은 벽돌이 없다면 더 이상 진행할 필요가 없다
    #  - (마찬가지로) 현재 남은 벽돌 수를 저장
    # 3. N번 구슬을 쏘자
    #  - 시작점 : 0번 / 하나도 안깨진 벽돌 수
    #  - 끝점 : N번 쏘면 끝 / 벽돌이 다 깨지면 끝

    min_left = 1e9          # 최소 벽돌 개수 저장
    curr_left = 0           # 남은 벽돌이 없다면 더 이상 진행할 필요가 없다 -> 현재 남은 벽돌 수 같이 저장
    # curr_left 갱신
    for row in arr:
        for el in row:
            if el:
                curr_left += 1

    shoot(0, curr_left, arr)

    print(f'#{t} {min_left}')