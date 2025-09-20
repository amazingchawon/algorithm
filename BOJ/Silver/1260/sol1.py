# [S2] 1260 DFS와 BFS
from collections import deque

# STEP 1. 입력 받기
N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

# STEP 1.1. 그래프 만들기
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1

# STEP 2. DFS 구현
def dfs(start):
    visited = [0] * (N+1)
    stack = [start]

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = 1
            print(node, end=" ")

            for i in range(N, 0, -1):   # 작은 정점부터 방문하기 위해 역순으로 순회
                if graph[node][i] and visited[i] != 1:
                    stack.append(i)


# STEP 3. BFS 구현
def bfs(start):
    visited = [0] * (N+1)
    q = deque([start])
    visited[start] = 1

    while q:
        node = q.popleft()
        print(node, end=" ")

        for i in range(1, N+1):
            if graph[node][i] and visited[i] != 1:
                q.append(i)
                visited[i] = 1

dfs(V)
print()
bfs(V)