# [G3] 1238 파티
import heapq

# STEP 1. 입력 받기
N, M, X = map(int, input().split())

time = [[] for _ in range(N+1)]         # 도착 지점에서 돌아오는 값 연산할 때 쓰일 인접리스트
rtime = [[] for _ in range(N+1)]        # 도착 지점까지 가는 길 연산할 때 쓰일 인접리스트

for _ in range(M):
    s, e, v = map(int, input().split())
    time[s].append((e, v))
    rtime[e].append((s, v))

# STEP 2. dijkstra 코드
def dijkstra(graph, start):
    INF = 10**15
    dist = [INF] * (N+1)
    dist[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        curr_dist, curr_node = heapq.heappop(q)

        if dist[curr_node] < curr_dist:
            continue

        for nxt, nxt_dist in graph[curr_node]:
            tmp = curr_dist + nxt_dist
            if tmp < dist[nxt]:
                dist[nxt] = tmp
                heapq.heappush(q, (tmp, nxt))

    return dist

to_x = dijkstra(rtime, X)
from_x = dijkstra(time, X)
total = [-1] * (N+1)

for i in range(1, N+1):
    total[i] = to_x[i] + from_x[i]

print(max(total))