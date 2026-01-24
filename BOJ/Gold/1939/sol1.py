# [G3] 1939 중량제한

# STEP 1. 입력
N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    adj[b].append((a, c))

start, end = map(int, input().split())

answer = 0

# STEP 2. start - end 순회
visited = [0] * (N + 1)
stack = []
stack.append((start, 0))

while stack:
    curr, weight = stack.pop()
    if curr == end:
        answer = max(answer, weight)
        visited = [0] * (N+1)
        visited[start] = 1
        continue

    if not visited[curr]:
        visited[curr] = 1

        for next, limit in adj[curr]:
            if not visited[next]:
                if weight == 0:
                    stack.append((next, limit))
                else:
                    stack.append((next, min(weight, limit)))

print(answer)