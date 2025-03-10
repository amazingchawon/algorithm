# [G4] 1753 최단 경로

import heapq

inf = int(1e9)

# STEP 1. 입력 받기
V, E = map(int, input().split())
start = int(input())

graph = [[] for i in range(V+1)]
distance = [inf] * (V+1)

for _ in range(E):                          # 간선 정보 저장
    a, b, w = map(int, input().split())
    graph[a].append([b, w])

# STEP 2. 다익스트라 정의
def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))       # (누적값, 노드번호) heapq에 저장
    distance[start] = 0                     # 자기 자신은 0

    # 우선순위 큐가 빌 때 까지 반복
    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue

        for next in graph[now]:
            next_node, cost = next

            new_cost = dist + cost

            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, V+1):
    # 도달 할 수 없는 경우, 무한 출력
    if distance[i] == inf:
        print('INF')
    else:
        print(distance[i])