# [D3] 5250 최소 비용
# 테스트케이스 10개 중 4개만 정답처리

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def BFS(start, end):
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()

        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            new_cost = cost[x][y] + 1
            # 범위 안인지 확인
            if 0 <= nx < N and 0 <= ny < N:
                if arr[x][y] > arr[nx][ny]:             # 다음 칸이 더 낮다면
                    pass
                else:                                   # 다음 칸이 더 높다면
                    new_cost += arr[nx][ny] - arr[x][y] # 높이 차이만큼 더해주기

                # 다음 칸에 적힌 연료값보다 x, y 에서 이동하는게 적게 든다면
                if cost[nx][ny] > new_cost:
                    cost[nx][ny] = new_cost
                    q.append((nx, ny))


INF = int(1e9)
T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cost = [[INF] * N for _ in range(N)]
    cost[0][0] = arr[0][0]

    BFS((0, 0), (N-1, N-1))

    print(f'#{t} {cost[N-1][N-1]}')

