# [D2] 5102 노드의 거리

import sys
sys.stdin = open('input.txt', 'r')

def BFS(start, goal):
    global result

    queue = [start]

    while queue:
        current = queue.pop(0)

        # 종료 조건 : goal 도착했을 때
        if current == goal:
            result = visited[goal]
            return

        for next in range(V+1):
            if adj[current][next] and visited[next] == 0:
                queue.append(next)
                visited[next] = visited[current] + 1


T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())

    # STEP 1. 인접행렬 만들기
    adj = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        adj[v1][v2] = 1
        adj[v2][v1] = 1

    # STEP 2. BFS 탐색
    result = 0
    visited = [0] * (V+1)
    S, G = map(int, input().split())
    BFS(S, G)

    print(f'#{t} {result}')