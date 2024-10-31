# [LV2] 49189 가장 먼 노드
from collections import deque


def solution(n, edge):
    answer = 0
    visited = [0] * (n+1)
    adj = [[] for _ in range(n+1)]
    q = deque()

    # STEP 1. 인접 리스트 만들기
    for v1, v2 in edge:
        adj[v1].append(v2)
        adj[v2].append(v1)
        # 만약 1번 노드와 연결된 노드라면, 바로 visited 배열 숫자 넣어주기 + q에 추가
        if v1 == 1:
            visited[v2] = 1
            q.append(v2)
        elif v2 == 1:
            visited[v1] = 1
            q.append(v1)

    # STEP 2. 노드 순회
    while q or visited.count(0) > 2:
        current = q.popleft()
        for node in adj[current]:
            if node != 1 and visited[node] == 0:
                q.append(node)
                visited[node] = visited[current] + 1

    distance = max(visited)
    answer = visited.count(distance)
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))