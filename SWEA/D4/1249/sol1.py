# [D4] 1249 보급로

import sys
import heapq
sys.stdin = open('input.txt', 'r')

T = int(input())
INF = 1e9


def dijkstra(start_x, start_y):
    pq = []
    
    heapq.heappush(pq, (0, (start_x, start_y)))
    distance[start_x][start_y] = 0
    
    while pq:
        dist, position = heapq.heappop(pq)
        x, y = position

        if visited[x][y] == 1:
            continue
        else:
            visited[x][y] = 1

        # 이미 갱신되어 있는 위치라면 -> 넘어가기
        if distance[x][y] < dist:
            continue

        # 마지막 칸 도달하면 종료
        if x == N-1 and y == N-1:
            break

        # 상하좌우 탐색
        for dx, dy in [(-1,0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            # 범위 안이라면,
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                # cost : 가중치 얼마인지 저장, new_cost : 누적 가중치 저장
                cost = arr[nx][ny]
                new_cost = dist + cost

                # 원래 다음 칸에 가는게 비용이 얼마나 드는지 확인
                # new_cost가 더 적으면 갱신
                if new_cost <= distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(pq, (new_cost, (nx, ny)))


for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 다익스트라 알고리즘
    # 각 칸별로 누적거리 저장할 테이블
    distance = [[INF] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dijkstra(0, 0)
    
    answer = distance[N-1][N-1]
    print(f'#{t} {answer}')