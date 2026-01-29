# [G3] 1238 파티
import heapq

# STEP 1. 입력 받기
N, M, X = map(int, input().split())

time = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    s, e, v = map(int, input().split())
    time[s][e] = v

INF = 1e8
time_to_x = [INF] * (N+1)
time_from_x = [INF] * (N+1)

# STEP 2. 다익스트라
def dijkstra_to_x(start):
    q = []
    heapq.heappush(q, (0, start))
    time_to_x[start] = 0

    while q:
        dist, now = heapq.heappop(q)                # 우선순위가 가장 낮은 값이 나온다.

        if time_to_x[now] < dist:                   # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
            continue                                # 따라서 다음으로 넘어간다.

        for nxt in range(1, N+1):                   # 연결된 모든 노드 탐색
            if time[nxt][now]:
                tmp = dist + time[nxt][now]

                if tmp < time_to_x[nxt]:
                    time_to_x[nxt] = tmp
                    heapq.heappush(q, (tmp, nxt))


def dijkstra_from_x(start):
    q = []
    heapq.heappush(q, (0, start))
    time_from_x[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if time_from_x[now] < dist:
            continue

        for nxt in range(1, N + 1):
            if time[now][nxt]:
                tmp = dist + time[now][nxt]

                if tmp < time_from_x[nxt]:
                    time_from_x[nxt] = tmp
                    heapq.heappush(q, (tmp, nxt))


dijkstra_to_x(X)
dijkstra_from_x(X)

total = [0] * N
for i in range(N):
    total[i] = time_to_x[i+1] + time_from_x[i+1]

print(max(total))