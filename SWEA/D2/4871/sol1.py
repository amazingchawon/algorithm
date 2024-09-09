# [D2] 4871 그래프 경로

import sys
sys.stdin = open('input.txt', 'r')


def DFS(current, end):
    global result
    visited[current] = 1

    # 기저 조건
    # 현재 노드가 종료 노드와 같다면
    if current == end:
        result = 1
        return

    for next in range(V+1):
        if adj[current][next] and visited[next] == 0:
            DFS(next, end)

T = int(input())

for t in range(1, T+1):
    # V : 노드 개수, E : 간선 개수
    V, E = map(int, input().split())

    # STEP 1. 인접행렬 만들기
    adj = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        adj[v1][v2] = 1

    # STEP 2. DFS 탐색
    S, G = map(int, input().split())
    result = 0
    visited = [0] * (V+1)
    DFS(S, G)

    print(f'#{t} {result}')